import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Get the table.
table = dynamodb.Table('battle-royal')
username="johnsonscott"
resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk AND SK = :metadata",
    ExpressionAttributeValues={
        ":pk": f"USER#{username}",
        ":metadata": f"#METADATA#{username}",
    },
)

print(resp)