terraform {
  source = "../../../iac-modules/aws-eks"
}

include {
  path   = find_in_parent_folders()
  expose = true
}

inputs = {
  subnet_ids      = "${include.inputs.subnet_ids}"
  cluster_name    = "k8s-cluster"
  cluster_version = "1.33"
}
