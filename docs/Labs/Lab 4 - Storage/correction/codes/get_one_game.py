import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Get the table.
table = dynamodb.Table('battle-royal')
game="c9c3917e-30f3-4ba4-82c4-2e9a0e4d1cfd"
resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk",
    ExpressionAttributeValues={
        ":pk": f"GAME#{game}"    },
)

print(len(resp["Items"]))


resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk AND begins_with(SK, :sk)",
    ExpressionAttributeValues={
        ":pk": f"GAME#{game}",
        ":sk": "USER#"    },
)

print(len(resp["Items"]))

