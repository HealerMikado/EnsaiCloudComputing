import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Get the table.
table = dynamodb.Table('battle-royal')
username="johnsonscott"
resp = table.query(
    IndexName="InvertedIndex",
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="SK = :sk",
    ExpressionAttributeValues={
        ":sk": f"USER#{username}"    },
)

print(resp["Items"])