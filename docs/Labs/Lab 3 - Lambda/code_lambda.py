import json
import boto3
from datetime import datetime

print('Loading function')


def lambda_handler(event, context):
    print(event)
    number1 = int(json.loads(event["Records"][0]["body"])["number1"])
    number2 = int(json.loads(event["Records"][0]["body"])["number2"])
    operation = json.loads(event["Records"][0]["body"])["operation"]
    if operation == "+":
        res = number1 + number2
    elif operation == "-":
        res = number1 - number2
    elif operation == "-":
        res = number1* number2
    elif operation == "/":
        res = number1/ number2
    else  :
        raise Exception('No a good operator')
        
    sqs = boto3.client('sqs')  #client is required to interact with 
    sqs.send_message(
       QueueUrl="https://sqs.us-east-1.amazonaws.com/675696485075/lab-output-queue",
       MessageBody=json.dumps({"result" : res})
    )
    return {
        'statusCode': 200,
        'body': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }
