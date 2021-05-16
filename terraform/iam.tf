resource "aws_iam_role" "s3_role" {
  name = "s3_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Sid": ""
    }
  ]
}
EOF

  tags = {
    tag-key = "s3-role"
  }
}

resource "aws_iam_instance_profile" "ssh_box_instance_profile" {
  name = "ssh_box_instance_profile"
  role = "s3_role"
}

resource "aws_iam_role_policy" "ssh_box_iam_role_policy" {
  name   = "ssh_box_iam_role_policy"
  role   = aws_iam_role.s3_role.id
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": ["arn:aws:s3:::setup-files-bucket"]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject"
      ],
      "Resource": ["arn:aws:s3:::setup-files-bucket/*"]
    }
  ]
}
EOF
}
