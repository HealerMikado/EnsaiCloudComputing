# Read file
import json
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Get the table.
table = dynamodb.Table('battle-royal')

# items = []
# with table.batch_writer() as batch:
#     with open('./items.json', 'r') as f:
#         for row in f:
#             batch.put_item(
#                 Item=json.loads(row)
#             )


response = table.scan(
    Select='COUNT',
    ReturnConsumedCapacity='TOTAL',
)

print(json.dumps(response, indent=2))

username = "johnsonscott"

resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk",
    ExpressionAttributeValues={
    ":pk": f"USER#{username}",
    },
     ReturnConsumedCapacity='TOTAL',
)

print(json.dumps(resp, indent=2))


response = table.scan(
    ExpressionAttributeValues={
        ':pk': f"USER#{username}",
    },
    FilterExpression='PK = :pk',
     ReturnConsumedCapacity='TOTAL',
) 

print(json.dumps(response, indent=2))


gameid = "c9c3917e-30f3-4ba4-82c4-2e9a0e4d1cfd"

resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk",
    ExpressionAttributeValues={
    ":pk": f"GAME#{gameid}",
    },
     ReturnConsumedCapacity='TOTAL',
)

print(resp)

resp = table.query(
    Select='ALL_ATTRIBUTES',
    IndexName='InvertedIndex',
    KeyConditionExpression="SK = :sk",
    ExpressionAttributeValues={
    ':sk': f"USER#{username}",
    },
     ReturnConsumedCapacity='TOTAL',
)

print(json.dumps(resp, indent=2))


response = table.scan(
    ExpressionAttributeValues={
        ':sk': f"USER#{username}",
    },
    FilterExpression='SK = :sk',
     ReturnConsumedCapacity='TOTAL',
) 

print(json.dumps(response, indent=2))
