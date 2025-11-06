from functions.create_task import lambda_handler
from logging import getLogger
import json

logger = getLogger()

event = {
    "body": json.dumps({ 
        "title": "Task 3",
        "description": "Probando local",
        "status": "pending"
    })
}


response = lambda_handler(event, None)
logger.info("Create Task Response: %s", response)
print(response)