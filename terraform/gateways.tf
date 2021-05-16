resource "aws_internet_gateway" "workshop_net_gw" {
  vpc_id = aws_vpc.workshop_net.id

  tags = {
    Name = "workshop_net_gw"
  }
}
