import os
import boto3
import base64
import time

bucket_name = os.environ['BUCKET_NAME']
slack_token = os.environ['SLACK_API_TOKEN']
slack_channel_id = os.environ['SLACK_CHANNEL_ID']
rekognition_collection_id = os.environ['REKOGNITION_COLLECTION_ID']


def decode(event, context):
    face = base64.b64decode(event['image_string'])
    s3 = boto3.client('s3')
    file_name = 'incoming/image-'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
    response = s3.put_object(Body=face, Bucket=bucket_name, Key=file_name)
    print(response)
    file_url = 'https://s3.amazonaws.com/' + bucket_name + '/' + file_name
    return file_url
