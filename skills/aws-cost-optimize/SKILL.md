---
name: aws-cost-optimize
description: >
  Analyzes AWS infrastructure (IaC Terraform/CDK or CloudWatch metrics) to identify cost optimizations and automatically create
  remediation plans and GitHub issues. Use when auditing AWS spend, reducing cloud infrastructure costs, or when user mentions
  "aws-cost-optimize", "aws cost audit", "reduce aws bill", or "iac cost optimization".
argument-hint: "[audit|iac|ec2|s3|remediation]"
license: MIT
---

# AWS Cost Optimize — Cloud Cost Audit & Optimization

Based on [github/aws-cost-optimize](https://skillrepo.dev/skills/github/aws-cost-optimize) (v1.0B), this skill audits AWS IaC templates and resource utilization.

## Optimization Vectors

- **Compute Right-Sizing**: Identifies over-provisioned EC2 instances and ECS tasks based on CPU/RAM metrics.
- **Storage Lifecycle Rules**: Moves stale S3 objects to Glacier Flexible/Deep Archive.
- **Idle Resource Cleanup**: Flags unattached EBS volumes, unused Elastic IPs, and orphaned NAT Gateways.
