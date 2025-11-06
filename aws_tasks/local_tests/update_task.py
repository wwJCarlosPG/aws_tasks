from functions.update_task import lambda_handler
from logging import getLogger
import json

logger = getLogger()

event = {
    "pathParameters": {"task_id": "5a68cd16-f3e9-465e-a5cf-ce0ad67c69aa"},
    "body": json.dumps({
        "title": "Updated Task Title",
        "description": "Updated description",
        "status": "completed"
    })
    }



response = lambda_handler(event, None)
logger.info("Create Task Response: %s", response)
print(response)