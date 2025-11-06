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
```git
git clone https://github.com/wwJCarlosPG/aws_tasks
```
Then:
```
cd aws_tasks
```

### Setup environment variables
Inside the ```aws_tasks``` directory, create a ```.env``` file and add the following line:
```bash
TABLE_NAME=TasksTable
```

### Build the Lambda Layer
Run the build script to install dependencies inside a compatible Amazon Linux 2 environment.
```bash
bash build_layer.sh
```
This step ensures that all Python dependencies (like ```pydantic``` and ```python-dotenv```)
are compiled for AWS Lambda’s runtime.

### Configure AWS credentials
If is your first time using the AWS CLI, configure your account:
```bash
aws configure
```
Ensure that the IAM user or role you use has sufficient permissions to:
- Deploy AWS CDK stacks (e.g., CloudFormation, IAM, Lambda, API Gateway, and DynamoDB).
- Create and manage AWS resources defined in the stack.
- Read and write to the target DynamoDB table.

It is recommended that the user has the AdministratorAccess policy attached, or equivalent custom permissions, to simplify deployment and avoid permission-related errors.
### Bootstrap the AWS environment (Optional)
If this is your first time deploying CDK resources in your AWS account, run:
```bash
cdk bootstrap aws://<account-id>/<region>
```

### Deploy the stack
Deploy the full solution:
```bash
cdk deploy
```
Once complete, the console will display the API endpoint URL, with the form:
```
https://<api-id>.execute-api.<region>.amazonaws.com/prod/
```
## Testing the API
You can test the API using Postman or curl:
### Examples

#### GET with curl
```
curl -X GET https://<api-id>.execute-api.<region>.amazonaws.com/prod/tasks/<task_id>
```
#### GET with Postman
- Select ```GET``` operation
- Write the following route:
  ```
  https://<api-id>.execute-api.<region>.amazonaws.com/prod/tasks/<task_id>
  ```
#### POST with curl
```bash
curl -X POST \
  https://<api-id>.execute-api.<region>.amazonaws.com/prod/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Title of the task",
    "description": "Description of the task",
    "status": "Status of the task"
  }'
```
#### POST with Postman
- Select ```POST``` operation
- Write the following route:
  ```bash
  https://<api-id>.execute-api.<region>.amazonaws.com/prod/tasks
  ```
- In Headers section fill ```Content-Type```(Key) and ```application/json```(Value)
- In Body (```raw``` option) type:
  ```bash
    {
    "title": "Title of task",
    "description": "Description of task",
    "status": "Status of task"
    }
  ```
#### PUT with curl
```bash
curl -X PUT \
  https://<api-id>.execute-api.<region>.amazonaws.com/prod/tasks/<task_id> \
  -d '{
    "title": "New title of the task",
    "description": "New description of the task",
    "status": "New status of the task"
  }'
```
#### PUT with Postman
- Select ```PUT``` operation
- Write the following route:
  ```bash
  https://<api-id>.execute-api.<region>.amazonaws.com/prod/tasks/<task_id>
  ```
- In Body (```raw``` option) type:
  ```bash
    {
    "title": "New title of task",
    "description": "New description of task",
    "status": "New status of task"
    }
  ```




