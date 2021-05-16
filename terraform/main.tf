terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_instance" "workshop_ec2_instance" {
  ami                  = "ami-0567f647e75c7bc05" // Amazon ubuntu
  instance_type        = "t2.micro"
  key_name             = aws_key_pair.deployer.key_name
  security_groups      = ["${aws_security_group.ingress_all_group.id}"]
  iam_instance_profile = aws_iam_instance_profile.ssh_box_instance_profile.id
  subnet_id            = aws_subnet.subnet_1.id

  user_data = templatefile("init.sh", { num_players = var.number_of_players, ctfd_api_key = var.ctfd_api_key })

  tags = {
    Name = "ubuntu-ssh-box"
  }
}
