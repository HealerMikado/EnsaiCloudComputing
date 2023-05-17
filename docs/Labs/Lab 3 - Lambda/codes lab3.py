# Code lambda

import json
import os
print('Loading function')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print(os.getenv("foo"))
    return event['key1']  # Echo back the first key value

##########################################################
# Code pour déployer une lambda avec cdktf

from cdktf_cdktf_provider_aws.lambda_function import LambdaFunction
class LambdaStack(TerraformStack):
    def init(self, scope: Construct, id: str):
        super().init(scope, id)
        AwsProvider(self, "AWS", region="us-east-1")

        # Packagage du code
        code = TerraformAsset(
            self, "code",
            path="./lambda", # dossier du code
            type= AssetType.ARCHIVE
        )

        # Create Lambda function
        lambda_function = LambdaFunction(self,
                "lambda",
                function_name="first_lambda",
                runtime="python3.8",
                memory_size=128,
                timeout=60,
                role="arn:aws:iam::ID_COMPTE:role/LabRole",
                filename= code.path,
                handler="lambda_function.lambda_handler",
                environment={"variables":{"foo":"bar"}}
            )
app = App()
LambdaStack(app, "cdktf_lambda")
app.synth()

##########################################################
# Code pour déployer une lambda et une file SQS
from cdktf_cdktf_provider_aws.sqs_queue import SqsQueue
class LambdaStack(TerraformStack):
    def init(self, scope: Construct, id: str):
        super().init(scope, id)
        AwsProvider(self, "AWS", region="us-east-1")
        # Packagage du code
        code = TerraformAsset(...)
        # Create Lambda function
        lambda_function = LambdaFunction(...)
        # Create SQS queue
        queue = SqsQueue(
            self,
            "queue",
            name="input_queue",
            visibility_timeout_seconds=60
        )
        # Link SQS as Lambda's source
        LambdaEventSourceMapping(
            self, "event_source_mapping",
            event_source_arn=queue.arn,
            function_name=lambda_function.arn
        )
app = App()
LambdaStack(app, "cdktf_lambda")
app.synth()

##########################################################
# Send message to sqs in lambda
import json
import boto3
from datetime import datetime
sqs = boto3.client('sqs')  #client is required to interact with sqs

def lambda_handler(event, context):
    # event provenant d'une lambda
    data = int(json.loads(event["Records"][0]["body"])["data"])

    sqs.send_message(
        QueueUrl="VOTRE URL SQS",
        MessageBody=json.dumps({"body" : data})
    )
    return {
        'statusCode': 200,
        'body': data
    }

##########################################################
# Code du test 
{
  "Records": [
    {
      "messageId": "bc8007e9-6a6d-41d4-ba09-2fcf16e5e6c3",
      "receiptHandle": "AQEB92BoJQllWCtZSiiIQ69fXXX4ac7cpxxcbTirw4/b+ziBTzAxlwXFMbj3w6wbOPom4jPusM9453dZDXi4iVH/vf97fFk6yg/EkP9UZRYrK5OwfWiIxQJkklWe8ZKK84uYVhGIDi5kBfWTCnsX6u83+GE59g/UWc0+jbYvOArOLwCCOTRqbH3spkG/GhDHlyxVwPv/K+xNM+7pqQX21yjSQdiLwwlk7dDJwiNGatRq9D1vIDHduabmHn2I1sLrq778ZkZXS4YJ6IYeFXC+kWVYlSy+lXyVxHfxBVXQcU8PsSNv6MsoBDgjU1LD43NFikQLVI5F/+HnBEX2AzhoJPBMz/eijKW1miJNZ48G9gg2H2DOt0x2OQtg2M2VqtxROmD06gHUPsr67vvBH2J5m77Oxw==",
      "body": "{\n\"number1\":1,\n\"number2\":5,\n\"operation\":\"+\"\n}",
      "attributes": {
        "ApproximateReceiveCount": "18",
        "SentTimestamp": "1681393246569",
        "SenderId": "AROAZ2UVGELJYYC7FJZIV:user2476414=__tudiant_test",
        "ApproximateFirstReceiveTimestamp": "1681393246569"
      },
      "messageAttributes": {},
      "md5OfBody": "cb76cceb2fbc7622690cdf4f256ea8e0",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:675696485075:lab-input-queue",
      "awsRegion": "us-east-1"
    }
  ]
}

##########################################################
# Code du message 
{"number1":1,"number2":5,"operation":+}