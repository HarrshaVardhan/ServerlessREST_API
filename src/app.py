import json


def app(event, context):
    response = {
        'statusCode': 200,
        'body': "Service is running!"
    }
    return response
