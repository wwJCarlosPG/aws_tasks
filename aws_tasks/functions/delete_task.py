from dotenv import load_dotenv
import boto3
import json
import os

load_dotenv()

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ['TABLE_NAME'])


def lambda_handler(event, context):
    """Delete a task from the DynamoDB table."""

    task_id = event['pathParameters']['task_id']
    if not task_id:
        return{
            'statusCode':400,
            'body': json.dumps({'error':'task_id is required'})
        }
    try:
        response = table.delete_item(Key={'task_id': task_id}, ReturnValues="ALL_OLD")
        if "Attributes" in response:
            return {
                "statusCode": 204,
                "body": "No Content"
            }
        else: 
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Task not found."})
            }
    except Exception as e:
        return{
            "statusCode": 500,
            "body": json.dumps({"error": "Server error."})
        }


