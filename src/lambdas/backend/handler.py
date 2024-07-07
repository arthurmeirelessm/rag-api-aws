import json
from typing import Any, Dict



def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    print(event)
    return event
