import json
import boto3
import base64
import os
from botocore.exceptions import NoCredentialsError

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Retrieve the file data (encoded in base64) and file name from the event
    file_content = event.get('file_content')
    file_name = event.get('file_name')
    bucket_name = os.environ.get('S3_BUCKET_NAME')  # Set your S3 bucket name in Lambda environment variables

    if not file_content or not file_name:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing file content or file name')
        }

    try:
        # Decode the base64 file content
        file_data = base64.b64decode(file_content)
        
        # Upload the file to the S3 bucket
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_data, ContentType="application/pdf")

        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} uploaded successfully.')
        }

    except NoCredentialsError:
        return {
            'statusCode': 403,
            'body': json.dumps('No AWS credentials found')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
