import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Get the table.
table = dynamodb.Table('battle-royal')

response = table.scan(
    Select='COUNT',
    ReturnConsumedCapacity='TOTAL',
)

print(response)