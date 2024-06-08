import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Get the table.
table = dynamodb.Table('battle-royal')
map="Green Grasslands"
resp = table.query(
    IndexName="Secondary",
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression="#m = :map",
    ExpressionAttributeNames={
        '#m': 'map'
    },
    ExpressionAttributeValues={
        ":map": map,},
)

print(resp["Items"])