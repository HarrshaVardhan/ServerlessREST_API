import os
import boto3
from datetime import date, timedelta

def date_just(timestamp):
    return timestamp.strftime("%d/%m/%Y")

def query(event, context):
    bucket_name = os.environ['BUCKET_NAME']
    print(bucket_name)
    client = boto3.client('dynamodb')
    timestamp_week_ago = date.today() - timedelta(days=7)
    timestamp_current = date.today()
    timestamp_week_ago = date_just(timestamp_week_ago)
    timestamp_current = date_just(timestamp_current)
    stmnt = f"SELECT * FROM notes WHERE CreatedAt BETWEEN '{timestamp_week_ago}' AND '{timestamp_current}'"
    response = client.execute_statement(Statement= stmnt)
    x=len(response["Items"])
    output=f"The number of added in a week ago : {x} Item/s on {bucket_name}"
    return output
