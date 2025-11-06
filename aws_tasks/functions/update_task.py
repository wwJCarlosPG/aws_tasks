from botocore.exceptions import ClientError
from pydantic import ValidationError
from dotenv import load_dotenv
from functions.models import Task
import boto3
import json
import os

load_dotenv()
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    task_id = event['pathParameters']['task_id']
    body = json.loads(event['body'])
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
        return{
            "statusCode": 400,
            "body": e.json()
        }

    try:
        response = table.update_item(
            Key={"task_id": task_id},
            UpdateExpression="SET title = :t, description = :d, #s = :s",
            ExpressionAttributeValues={
                ":t": validated_task.title,
                ":d": validated_task.description,
                ":s": validated_task.status
            },
            ExpressionAttributeNames={
                "#s": "status"
            },
            ConditionExpression="attribute_exists(task_id)",
            ReturnValues="ALL_NEW"
        )
        
        updated_item = response['Attributes']
        return{
            "statusCode": 200,
            "body": json.dumps(updated_item)
        }
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return{
                "statusCode": 404,
                "body": json.dumps({"error": "Task not found."})
            }
        else:
            return{
                "statusCode": 500,
                "body": json.dumps({"error": str(e)})
            }
