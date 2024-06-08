import json
import boto3
dynamodb = boto3.resource('dynamodb')

items = []
# ouvrir
with open("items.json", "r") as file :
    # boucle ligne
    for line in file : 
        items.append(json.loads(line))

print(items)


# Get the table.
table = dynamodb.Table('battle-royal')
# Batch writing item. Only one big query, cost less ans it's quicker
with table.batch_writer() as batch:
    for item in items:
        batch.put_item(
            Item=item
    )