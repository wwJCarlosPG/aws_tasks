from functions.models import Task
from dotenv import load_dotenv
import boto3 
import json
import os
from logging import getLogger
load_dotenv()
logger = getLogger()
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ['TASKS_TABLE'])


def lambda_handler(event, context):
    """Retrieve a task from the DynamoDB table."""
    task_id  = event['pathParameters']['task_id']

    if not task_id:
        return{
            'statusCode':400,
            'body': json.dumps({'error':'task_id is required'})
        }
    response = table.get_item(Key={'task_id': task_id})
    
    if "Item" in response:
        # Validate and serialize the task data
        validated_task = Task(**response["Item"])
        return {
            "statusCode": 200,
            "body": validated_task.model_dump_json()
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Task not found."})
        }
