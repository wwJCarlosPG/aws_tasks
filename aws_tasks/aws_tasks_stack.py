from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_apigateway as apigateway
)
from constructs import Construct
import os

class AwsTasksStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = dynamodb.Table(
            self, 'Tasks_Table',
            table_name= os.environ.get('TABLE_NAME', 'TasksTable'),
            partition_key = {"name": "task_id", "type": dynamodb.AttributeType.STRING},
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        layer = lambda_.LayerVersion(
            self, 'TasksLayer',
            code=lambda_.Code.from_asset('layer'),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_13],
            description='A layer to share code between Lambda functions'
        )

        create_task = lambda_.Function(
            self, 'CreateTask',
            runtime = lambda_.Runtime.PYTHON_3_13,
            handler = "functions.create_task.lambda_handler",
            code = lambda_.Code.from_asset("aws_tasks"),
            layers = [layer],
            environment={ "TABLE_NAME": table.table_name }
        )
        table.grant_full_access(create_task)

        get_task = lambda_.Function(
            self, 'GetTask',
            runtime = lambda_.Runtime.PYTHON_3_13,
            handler = "functions.get_task.lambda_handler",
            code = lambda_.Code.from_asset("aws_tasks"),
            layers = [layer],
            environment={ "TASKS_TABLE": table.table_name }
        )
        table.grant_read_data(get_task)

        update_task = lambda_.Function(
            self, 'UpdateTask',
            runtime = lambda_.Runtime.PYTHON_3_13,
            handler = "functions.update_task.lambda_handler",
            code = lambda_.Code.from_asset("aws_tasks"),
            layers = [layer],
            environment={ "TASKS_TABLE": table.table_name }
        )
        table.grant_read_write_data(update_task)

        delete_task = lambda_.Function(
            self, 'DeleteTask',
            runtime = lambda_.Runtime.PYTHON_3_13,
            handler = "functions.delete_task.lambda_handler",
            code = lambda_.Code.from_asset("aws_tasks"),
            layers = [layer],
            environment={ "TASKS_TABLE": table.table_name }
        )
        table.grant_read_write_data(delete_task)

        api = apigateway.RestApi(
            self, 'TasksApi',
            rest_api_name = "Tasks Service"
        )

        tasks = api.root.add_resource("tasks")
        task = tasks.add_resource("{task_id}")
        tasks.add_method("POST", apigateway.LambdaIntegration(create_task))
        task.add_method("GET", apigateway.LambdaIntegration(get_task))
        task.add_method("PUT", apigateway.LambdaIntegration(update_task))
        task.add_method("DELETE", apigateway.LambdaIntegration(delete_task))