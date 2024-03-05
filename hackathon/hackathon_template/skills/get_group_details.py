def skill(account_id, group_id):
    import requests

    params = {
        'groupId': group_id
    }

    url = f'http://core-public.dev.spotinst.com:2000/aws/ec2/group?spotinstAccountId={account_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "TOKEN"
    }
    response = requests.get(url, headers=headers, params=params)
    print(response)
    return response.json()
