from functions.get_task import lambda_handler
from logging import getLogger
import json

logger = getLogger()

event = {
    "pathParameters": {
        "task_id": "5a68cd16-f3e9-465e-a5cf-ce0ad67c69aa"
    }
}

response = lambda_handler(event, None)
logger.info("Create Task Response: %s", response)
print(response)

# 5a68cd16-f3e9-465e-a5cf-ce0ad67c69aa
# 72085131-34d9-4bd7-bc35-47e298f46fd3