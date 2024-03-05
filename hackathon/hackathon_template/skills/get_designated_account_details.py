import json
from loguru import logger
def skill(account_id):
    logger.info(f"get account provider details: {account_id}")
    import requests

    params = {
        'accountId': 'act-ef5a3926'
    }

    url = 'http://localhost:7900/azure/compute/group/accountProvider'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzcG90aW5zdCIsImV4cCI6MTg5NDYxMjE5OSwiaWF0IjoxNTc5MjUyMTk5LCJ1aWQiOi0xLCJyb2xlIjoyLCJvaWQiOiI2MDYwNzk4NjU5MjEifQ.l5fjLRh3jsyzCDtlvUG3NozaDWEDjlRNH9jKoJU8hYc"
    }
    logger.info(f"Getting account details for account_id: {account_id}")
  #  response = requests.get(url, headers=headers, params=params)
   # print(response.json())

    if account_id == "act-ef5a3926":
        return {
                    "accountId": "act-ef5a3926",
                    "organizationId": 606079865921,
                    "type": "AWS",
                    "status": "valid"
                }
    else:
        return {
            {
                "accountId": "act-cec3a035",
                "organizationId": 606079865921,
                "type": "Azure",
                "status": "valid"
            }
    }