
resource "aws_subnet" "subnet_1" {
  cidr_block        = cidrsubnet(aws_vpc.workshop_net.cidr_block, 2, 1)
  vpc_id            = aws_vpc.workshop_net.id
  availability_zone = "ap-southeast-2a"

}

resource "aws_route_table" "route_table_workshop_net" {
  vpc_id = aws_vpc.workshop_net.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.workshop_net_gw.id
  }

  tags = {
    Name = "workshop_net_route_table"
  }
}

resource "aws_route_table_association" "subnet_association" {
  subnet_id      = aws_subnet.subnet_1.id
  route_table_id = aws_route_table.route_table_workshop_net.id
}
