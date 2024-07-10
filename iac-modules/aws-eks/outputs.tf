output "eks_cluster_endpoint" {
  value = aws_eks_cluster.cluster.endpoint
}

output "eks_cluster_name" {
  value = aws_eks_cluster.cluster.name
}
