import json
from typing import Any, Dict
from src.lambdas.embbedings.service.embbedings_service import EmbbedingsService

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    service = EmbbedingsService()
    return service.process_event()