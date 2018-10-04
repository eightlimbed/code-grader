//
// main.tf -- Configuration for the Users service on GCP
//

// GCP Configuration
provider "google" {
    version     = "~> 1.18"
    credentials = "${file("${var.credentials}")}"
    project     = "${var.gcp_project}"
    region      = "${var.gcp_region}"
}

// VPC Firewall Configuration
resource "google_compute_firewall" "firewall" {
    name = "firewall"
    network = "default"

    allow {
        protocol = "icmp"
    }

    allow {
        protocol = "tcp"
        ports    = ["5001", "80"]
    }

    source_ranges = ["0.0.0.0/0"]
}

