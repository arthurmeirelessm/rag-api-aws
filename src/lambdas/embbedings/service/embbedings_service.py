from typing import Dict, Any
import boto3
import json

class EmbbedingsService:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def process_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        try:
            response = self.s3.get_object(Bucket=bucket, Key=key)
            content = response['Body'].read().decode('utf-8')
            print(content)

            return {
                'statusCode': 200,
                'body': json.dumps({
                    "message": content.replace('\r\n', '\n')
                })
            }
        except Exception as e:
            print(e)
            print(f'Error getting object {key} from bucket {bucket}. '
                  'Make sure they exist and your bucket is in the same region as this function.')
            raise e

