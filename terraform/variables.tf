variable "region" {
  description = "AWS region"
  default     = "ap-southeast-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t3.micro"
}

variable "key_name" {
  description = "SSH key pair name"
  default     = "cloud-journey-key"
}

variable "ami_id" {
  description = "Ubuntu 22.04 AMI for ap-southeast-1"
  default     = "ami-0dbf91f0aff3d5d2f"
}
