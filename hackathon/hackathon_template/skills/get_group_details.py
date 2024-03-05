def skill(account_id, group_id):
    import requests

    params = {
        'groupId': 'sig-63c7dd3c'
    }

    url = 'http://core-public.dev.spotinst.com:2000/aws/ec2/group?spotinstAccountId=act-ef5a3926'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "TOKEN"
    }
    response = requests.get(url, headers=headers, params=params)
    print(response)
    return response.json()
