import json
from loguru import logger
def skill(account_id):
    logger.warning("WARNING")
    logger.info(f"Getting account details for account_id: {account_id}")
    return json.dumps({"account_id": "TEST"})
