resource "aws_key_pair" "deployer" {
  key_name   = "deployer_key"
  public_key = file(var.ssh_public_key_path)
}

resource "aws_security_group" "ingress_all_group" {
  name = "allow_ssh_sg"

  vpc_id = aws_vpc.workshop_net.id

  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]

    from_port = 22
    to_port   = 22
    protocol  = "tcp"
  }

  // Terraform removes the default rule
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
