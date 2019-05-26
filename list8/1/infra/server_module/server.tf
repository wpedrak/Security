variable "image_name" {
  description = "Name of image to create instances from."
}

variable "region" {
  description = "Region"
  default = "europe-west4"
}

variable "server_type" {
  description = "Server type to use for the main application server."
  default     = "f1-micro"
}

# resource "google_compute_network" "default" {
#   name = "security8"
# }

# resource "google_compute_firewall" "www_firewall" {
#   name    = "www-firewall"
#   network = "${google_compute_network.default.name}"
#   source_tags = ["server"]

#   allow {
#     protocol = "tcp"
#     ports    = ["22", "5000"]
#   }
# }

resource "google_compute_instance" "server" {
  name         = "www-server"
  machine_type = "${var.server_type}"
  zone         = "${var.region}-a"
  tags         = ["server"]

  boot_disk {
    initialize_params {
      image = "${var.image_name}"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }
}

output "public_ip" {
  value = "${google_compute_instance.server.network_interface.0.access_config.0.nat_ip}"
}