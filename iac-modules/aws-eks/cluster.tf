# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_cluster
resource "aws_eks_cluster" "cluster" {
  name     = var.cluster_name
  role_arn = aws_iam_role.eks_cluster_role.arn
  version  = var.cluster_version

  vpc_config {
    subnet_ids = var.subnet_ids
  }

  tags = merge(var.tags, {
    "Name" = "${var.cluster_name}"
  })

  depends_on = [
    aws_iam_role.eks_cluster_role
  ]

  lifecycle {
    ignore_changes = [
      name,
      tags
    ]
  }
}
