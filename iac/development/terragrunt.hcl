locals {
  environment = "dev"

  aws_account_id = "071646905294"
  aws_profile    = "dev"
  aws_region     = "us-west-2"
  subnet_ids     = ["subnet-068d962ddf711831b", "subnet-01b3f9553c3dc6bfd", "subnet-0eb4d12e888eaeb02", "subnet-0e538381f9607f225"]

  tags = {
    CostCenter  = "12345"
    Environment = "dev"
    Application = "IaC"
    createdBy   = "Alex"
    createdWith = "Terraform"
  }
}

generate "provider" {
  path      = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents  = <<EOF

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = ">= 5.0.1"
    }
  }
}

provider "aws" {
  profile = "${local.aws_profile}"
  region  = "${local.aws_region}"
}
EOF
}

remote_state {
  backend = "s3"
  config = {
    bucket  = "alex-terraform-state-personal"
    key     = "${path_relative_to_include()}/terraform.tfstate"
    region  = "${local.aws_region}"
    profile = "${local.aws_profile}"
    encrypt = true
  }
  generate = {
    path      = "backend.tf"
    if_exists = "overwrite_terragrunt"
  }
}

inputs = merge(
  {
    tags = local.tags
    aws_region = local.aws_region,
    subnet_ids = local.subnet_ids,
    aws_account_id = local.aws_account_id,
    environment = local.environment
    #vpc_id     = local.vpc_id
  }
)