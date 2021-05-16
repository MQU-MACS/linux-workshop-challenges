resource "aws_s3_bucket" "setup_files" {
  bucket = "setup-files-bucket"
  acl    = "private"

  tags = {
    Name = "setup-files-bucket"
  }
}

resource "aws_s3_bucket_object" "setup_files" {
  bucket = aws_s3_bucket.setup_files.id

  for_each = fileset("../setup-files/", "**")

  key    = "setup-files/${each.value}"
  source = "../setup-files/${each.value}"

  etag = filemd5("../setup-files/${each.value}")
}
