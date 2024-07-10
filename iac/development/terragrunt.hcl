locals {
  environment = "dev"

  aws_account_id = "0123456789"
  aws_profile    = "dev"
  aws_region     = "us-east-1"
  subnet_ids     = ["subnet-1", "subnet-2", "subnet-3", "subnet-4"]

  tags = {
    CostCenter  = "12345"
    Environment = "dev"
    Application = "IaC"
    createdBy   = "Alexander"
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
    bucket  = "terraform-state-12345678-bucket"
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