import os
import boto3
from datetime import date, timedelta

def date_just(timestamp):
    return timestamp.strftime("%d/%m/%Y")

def query(event, context):
    bucket_name = os.environ['BUCKET_NAME']
    client = boto3.client('dynamodb')
    timestamp_week_ago = date.today() - timedelta(days=7)
    timestamp_current = date.today()
    timestamp_week_ago = date_just(timestamp_week_ago)
    timestamp_current = date_just(timestamp_current)
    stmnt = f"SELECT * FROM notes WHERE CreatedAt BETWEEN '{timestamp_week_ago}' AND '{timestamp_current}'"
    qres = client.execute_statement(Statement= stmnt)
    x=len(qres["Items"])
    output=f"The number of added item/s in the last week : {x}"
    s3 = boto3.client('s3')
    fileName=str(timestamp_current) + '.txt'
    s3.put_object(Bucket=bucket_name, Key=fileName, Body=output)
    response = {
        'statusCode': 200,
        'body': "Report Added!"
    }
    return response
