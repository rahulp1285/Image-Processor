
provider "aws" {
#Access Keys can be passed via Secret Vault or AWS Secrets Manager
  region = "eu-west-1"
  access_key = "XXXXXXXXX"
  secret_key = "XXXXXXXXX/"
}


resource "aws_iam_user" "User1" {
  name = var.Usr1
  path = "/"

  tags = {
    access = "bucket-A"
  }
}



resource "aws_iam_user_policy" "policy1" {
  name = "policy1"
  user = aws_iam_user.User1.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:PutObject",
          "s3:GetObject"
        ]
        Effect   = "Allow"
        Resource = "arn:aws:s3:::BucketA/*"
      },
    ]
  })
}


resource "aws_iam_user" "User2" {
  name = var.Usr2
  path = "/"

  tags = {
    access = "bucket-B"
  }
}



resource "aws_iam_user_policy" "policy2" {
  name = "policy2"
  user = aws_iam_user.User2.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:Get*",
          "s3:List*"
        ]
        Effect   = "Allow"
        Resource = "arn:aws:s3:::BucketB/*"
      },
    ]
  })
}


