import json
import urllib.parse
import boto3

print('Loading function')

print('Preparing Boto3 Client Connection for S3')
s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        print('Fetch the Object and location from Original Bucket')
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE of the Object is : " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

     -----CAll Imageprocess.py -----


