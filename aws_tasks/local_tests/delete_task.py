from functions.delete_task import lambda_handler
from logging import getLogger
import json

logger = getLogger()

event = {
    "pathParameters": {"task_id": "72085131-34d9-4bd7-bc35-47e298f46fd3"}
    }



response = lambda_handler(event, None)
logger.info("Create Task Response: %s", response)
print(response)