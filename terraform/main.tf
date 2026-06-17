# Configure AWS Provider
provider "aws" {
  region = var.region
}

# Security Group
resource "aws_security_group" "cloud_journey_sg" {
  name        = "cloud-journey-tf-sg"
  description = "Security group managed by Terraform"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "cloud-journey-tf-sg"
    Project = "cloud-journey"
    ManagedBy = "terraform"
  }
}

# EC2 Instance
resource "aws_instance" "cloud_journey_ec2" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.cloud_journey_sg.id]

  tags = {
    Name      = "cloud-journey-tf-ec2"
    Project   = "cloud-journey"
    ManagedBy = "terraform"
  }
}

