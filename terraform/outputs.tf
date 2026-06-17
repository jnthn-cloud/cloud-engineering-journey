output "instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.cloud_journey_ec2.id
}

output "public_ip" {
  description = "EC2 Public IP Address"
  value       = aws_instance.cloud_journey_ec2.public_ip
}

output "security_group_id" {
  description = "Security Group ID"
  value       = aws_security_group.cloud_journey_sg.id
}

output "dashboard_url" {
  description = "Web Dashboard URL"
  value       = "http://${aws_instance.cloud_journey_ec2.public_ip}"
}
