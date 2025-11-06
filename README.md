# AWS Tasks API

This project implements a simple **Serverless Task Management API** using **AWS Lambda**, **DynamoDB**, and **AWS CDK (Cloud Development Kit)**.  
The API provides endpoints to create and retrieve tasks, following an event-driven and fully managed architecture.

---

## Project Overview

The infrastructure is defined using **AWS CDK (Python)**, which deploys:
- A DynamoDB table (`TasksTable`)
- Lambda functions for task management (e.g., `GetTask`, `CreateTask`)
- API Gateway to expose the Lambda functions as REST endpoints
- A Lambda Layer containing external dependencies

---

## Prerequisites

Before starting, make sure you have:

- **Python 3.13**
- **Node.js 18+** (for CDK)
- **AWS CDK CLI** installed:
  ```bash
  npm install -g aws-cdk
  ```
## Setup Instructions

### Clone the repository
git clone https://github.com/<your-username>/aws-tasks.git
cd aws-tasks



