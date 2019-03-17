provider "aws" {
  profile = "default"
  region  = "us-west-2"
}

resource "aws_instance" "www" {
  ami             = "ami-005bdb005fb00e791" # ubuntu 18.04
  instance_type   = "t2.micro"
  key_name        = "cloud2018"
  vpc_security_group_ids = ["${aws_security_group.www_group.id}"]

  tags {
    Name = "www"
  }
}

resource "aws_security_group" "www_group" {

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }

}


output "www_private_ips" {
  value = "${aws_instance.www.public_ip}"
}