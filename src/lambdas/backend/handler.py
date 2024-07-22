from typing import Dict, Any
import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    bucket = 'rag-api-aws'
    key = 'kb/rag-api-aws-kb.txt'
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        print(content)

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': "Ola tudo bem?"
            }
        
    except Exception as e:
        print(e)
        print(f'Error getting object {key} from bucket {bucket}. '
              'Make sure they exist and your bucket is in the same region as this function.')
        raise e
