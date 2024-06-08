import boto3
import json

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Get the table.
table = dynamodb.Table('battle-royal')

# SELECT COUNT(*) FROM  battle-royal
response = table.scan(
    Select='COUNT',
    ReturnConsumedCapacity='TOTAL',
)

print(json.dumps(response, indent=2))

# SELECT * FROM battle-royal WHERE PK='johnsonscott'
# SELECT * FROM battle-royal WHERE PK=%(name)s, name = johnsonscott

user="johnsonscott"
resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk",
    ExpressionAttributeValues={
        ":pk": f"USER#{user}",
    },
)

print(json.dumps(resp, indent=2))


response = table.get_item(
    Key={
        'PK': f"USER#{user}",
        'SK' : f"#METADATA#{user}"
    }
)

print(json.dumps(resp, indent=2))

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


response = table.get_item(
    Key={
        'PK': f"GAME#{game}",
        'SK' : f"#METADATA#{game}"
    }
)

print(resp)

#begins_with(col, val)
resp = table.query(
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="PK = :pk AND begins_with(SK, :sk)",
    ExpressionAttributeValues={
        ":pk": f"GAME#{game}",
        ":sk": f"USER#"
    },
)
print(json.dumps(resp, indent=2))


resp = table.query(
    Select='ALL_ATTRIBUTES',
    IndexName='InvertedIndex',
    KeyConditionExpression="SK = :sk AND begins_with(PK, :pk)",
    ExpressionAttributeValues={
        ":pk": f"GAME#",
        ":sk": f"USER#{user}"
    },
)
print(json.dumps(resp, indent=2))


resp = table.query(
    Select='ALL_ATTRIBUTES',
    IndexName='SecondaryIndex',
    KeyConditionExpression="#m = :map",
    ExpressionAttributeNames={
        '#m': 'map'
    },
    ExpressionAttributeValues={
        ":map": "Green Grasslands",
    },
)
print(resp)