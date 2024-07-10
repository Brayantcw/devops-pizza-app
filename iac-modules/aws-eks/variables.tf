variable "cluster_name" {
  type    = string
  default = "k8s-cluster"
}

variable "cluster_version" {
  type    = string
  default = "1.33"
}

variable "tags" {
  type    = map(string)
  default = null
}

variable "subnet_ids" {
  type    = list(string)
  default = null
}