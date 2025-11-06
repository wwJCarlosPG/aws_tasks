from pydantic import ValidationError
from functions.models import Task
from dotenv import load_dotenv
import boto3
import json 
import uuid
import os

load_dotenv()

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ['TABLE_NAME'])


def lambda_handler(event, context):
    """Create a new task in the DynamoDB table."""

    body = json.loads(event['body'])
    task_id = str(uuid.uuid4())
    task_item = {
        'task_id':task_id,
        'title':  body['title'],
        'description': body['description'],
        'status': body['status']
    }
    try:
        # Validate the task data
        validated_task = Task(**task_item)
    except ValidationError as e:
        return {
            'statusCode': 400,
            'body': e.json()
        }
    
    try:
        table.put_item(Item=validated_task.dict())

        return {
            'statusCode': 201,
            'body': validated_task.model_dump_json()
            }   
    except Exception as e:
        return{
            "statusCode": 500,
            "body": json.dumps({"error": "Server error.", "message": str(e)})
        }

