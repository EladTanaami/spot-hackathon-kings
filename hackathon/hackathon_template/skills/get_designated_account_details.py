import json
from loguru import logger
def skill(account_id):
    logger.info(f"Getting account details for account_id: {account_id}")
    return json.dumps({"account_id": "act-1", "cloud_provider": "AWS"})
