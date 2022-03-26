import ast
import boto3
from datetime import date

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('notes')
today = date.today()
d1 = today.strftime("%d/%m/%Y")


def add(event, context):
    data = event['body']
    item = ast.literal_eval(data)
    timestamp = {'date': d1}
    output=item.copy()
    for key, value in timestamp.items():
        output[key] = value
    table.put_item(Item=output)
    response = {
        "statusCode": 200,
        "body": "Item added!"
    }
    return response
