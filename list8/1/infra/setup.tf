provider "google" {
  project = "cloud2018-list2"
  region = "europe-west4"
}

variable "server_type" {
  description = "Server type to use for the main application server."
  default     = "f1-micro"
}

variable "image_name" {
  description = "Name of image."
  default     = "ubuntu-1810"
  # default     = "security8"
}

locals {
  region = "europe-north1"
}

module "server" {
  source = "./server_module/"
  
  image_name = "${var.image_name}"
  region = "${local.region}"
}

output "ip_of_server" {
    value = "${module.server.public_ip}"
}