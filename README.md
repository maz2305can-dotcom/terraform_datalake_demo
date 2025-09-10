# Terraform Data Lake Demo

This project provisions a simple **data lake environment** using Terraform and AWS resources.

# Project Structure
```
├── main.tf        # Terraform configuration for S3 + IAM
├── variables.tf   # Optional variables
└── README.md      # Documentation
```

# Requirements
- Terraform >= 1.3
- AWS CLI configured with credentials

# Usage

1. Initialize Terraform:
```bash
terraform init
```

2. Plan resources:
```bash
terraform plan
```

3. Apply configuration:
```bash
terraform apply -auto-approve
```

4. Destroy resources when done:
```bash
terraform destroy -auto-approve
```

# Resources Created
- **S3 Bucket** for storing raw/clean/curated data (data lake)
- **IAM Role** with policy for bucket access
- **Policy Attachment** linking role and S3 permissions

# References
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/index.html)

---
Author: Marcus Eberhardt  
maz2305@me.com  
[LinkedIn](https://linkedin.com/in/marcus-eberhardt-1401886)
