//
// vars.tf -- Contains variables that are used in the Users config
//

variable "credentials" { default = "./creds.json" }
variable "gcp_project" { default = "code-grader" }
variable "name"        { default = "prod" }
variable "gcp_region"  { default = "us-west1" }
variable "gcp_zone"    { default = "us-west1-a" }
