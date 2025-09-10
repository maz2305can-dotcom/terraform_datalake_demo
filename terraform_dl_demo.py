# -----------------------------
# FILE: main.tf
# -----------------------------


provider "aws" {
region = "us-east-1"
}


# S3 bucket for data lake
resource "aws_s3_bucket" "datalake" {
bucket = "demo-datalake-bucket-marcus"
acl = "private"


tags = {
Name = "demo-datalake"
Environment = "demo"
}
}


# Create Bronze, Silver, Gold folder prefixes
resource "aws_s3_object" "folders" {
for_each = toset(["bronze/", "silver/", "gold/"])
bucket = aws_s3_bucket.datalake.bucket
key = each.key
}


# IAM role for data lake access
resource "aws_iam_role" "datalake_role" {
name = "datalake-access-role"
assume_role_policy = <<EOF
{
"Version": "2012-10-17",
"Statement": [
{
"Action": "sts:AssumeRole",
"Principal": {
"Service": "ec2.amazonaws.com"
},
"Effect": "Allow",
"Sid": ""
}
]
}
EOF
}


# IAM policy for S3 access
resource "aws_iam_policy" "datalake_policy" {
name = "datalake-s3-policy"
description = "Policy for data lake S3 access"


policy = <<EOF
{
"Version": "2012-10-17",
"Statement": [
{
"Action": [
"s3:GetObject",
"s3:PutObject",
"s3:ListBucket"
],
"Effect": "Allow",
"Resource": [
"${aws_s3_bucket.datalake.arn}",
"${aws_s3_bucket.datalake.arn}/*"
]
}
]
}
}
