def skill(account_id, group_id):
    import requests

    params = {
        'groupId': group_id
    }

    url = f'http://core-public.dev.spotinst.com:2000/aws/ec2/group?spotinstAccountId={account_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzcG90aW5zdCIsImV4cCI6MTg5NDYxMjE5OSwiaWF0IjoxNTc5MjUyMTk5LCJ1aWQiOi0xLCJyb2xlIjoyLCJvaWQiOiI2MDYwNzk4NjU5MjEifQ.l5fjLRh3jsyzCDtlvUG3NozaDWEDjlRNH9jKoJU8hYc"
    }
    response = requests.get(url, headers=headers, params=params)
    print(response)
    return response.json()
