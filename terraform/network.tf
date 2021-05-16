resource "aws_vpc" "workshop_net" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "workshop_net"
  }
}

resource "aws_eip" "eip" {
  instance = aws_instance.workshop_ec2_instance.id
  vpc      = true
}
