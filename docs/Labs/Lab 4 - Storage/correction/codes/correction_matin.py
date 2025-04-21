import boto3
import json


# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Get the table.
table = dynamodb.Table('battle-royal')
# items=[]
# with table.batch_writer() as batch:
#     with open('items.json', 'r') as f:
#         for row in f:
#             batch.put_item(
#                 Item=json.loads(row)
#             )

response = table.scan(
Select='COUNT',
ReturnConsumedCapacity='TOTAL',
)

print(json.dumps(response, indent=2))

username="johnsonscott"
response = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk",
    ExpressionAttributeValues={
    ":pk": f"USER#{username}",
    },
    )

print(json.dumps(response, indent=2))


response = table.get_item(
    Key={
        'PK': f"USER#{username}",
        'SK' : f"#METADATA#{username}"
    }
)


print(json.dumps(response, indent=2))


game="292c8712-c9df-4721-a9a2-cae4ac607ed6"
resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk AND SK = :sk",
    ExpressionAttributeValues={
        ":pk": f"GAME#{game}",
        ":sk": f"#METADATA#{game}"
    },
)
print(resp)


game="292c8712-c9df-4721-a9a2-cae4ac607ed6"
resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk",
    ExpressionAttributeValues={
        ":pk": f"GAME#{game}",
    },
)
print(resp)
