import json
import boto3

# Batch upload
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Get the table.
table = dynamodb.Table('battle-royal')
# Read file
with open('items.json', 'r') as f:
    with table.batch_writer() as batch:
        for row in f:
            batch.put_item(Item=json.loads(row))
