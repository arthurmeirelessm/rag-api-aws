from typing import Dict, Any
import boto3
import json

class GenericHandler:
    def __init__(self):
        # Inicializa o cliente S3 (ou outros recursos necessários)
        self.s3 = boto3.client('s3')

    def process_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
       return ""
