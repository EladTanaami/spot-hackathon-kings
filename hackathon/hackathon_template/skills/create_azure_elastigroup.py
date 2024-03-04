"""
This skill creates an Azure Elastigroup in the specified account.
"""
import json
from loguru import logger


# TODO ADD AUTH TOKEN MANUALLY
def skill(account_id, group):
    logger.info(f"creating group: {group}")
    import requests

    url = 'http://localhost:3030/azure/compute/group?spotinstAccountId=act-cec3a035'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzcG90aW5zdCIsImV4cCI6MTg5NDYxMjE5OSwiaWF0IjoxNTc5MjUyMTk5LCJ1aWQiOi0xLCJyb2xlIjoyLCJvaWQiOiI2MDYwNzk4NjU5MjEifQ.l5fjLRh3jsyzCDtlvUG3NozaDWEDjlRNH9jKoJU8hYc"
    }

    # {
    #     "group": {
    #         "name": "elad-attributes-test1",
    #         "region": "eastus",
    #         "resourceGroupName": "Elad_RG1",
    #         "capacity": {
    #             "target": 2,
    #             "minimum": 0,
    #             "maximum": 3
    #         },
    #         "strategy": {
    #             "spotPercentage": 100,
    #             "drainingTimeout": 120,
    #             "fallbackToOd": True,
    #             "orientation": "availability",
    #             "revertToSpot": {
    #                 "performAt": "always"
    #             }
    #         },
    #         "compute": {
    #             "os": "Linux",
    #             "vmSizes": {
    #                 "odSizes": [
    #                     "standard_d2s_v3"
    #                 ],
    #                 "spotSizeAttributes": {
    #                     "minCpu": 2,
    #                     "maxCpu": 8,
    #                     "minStorage": 5,
    #                     "maxStorage": 1000,
    #                     "minMemory": 2,
    #                     "maxMemory": 32,
    #                     "cpuArchitecture": "X64"
    #                 },
    #                 "excludedVmSizes": [
    #                     "standard_d2s_v3",
    #                     "standard_d2s_v3"
    #                 ]
    #             },
    #             "launchSpecification": {
    #                 "dataDisks": [
    #                     {
    #                         "sizeGB": 1,
    #                         "lun": 1,
    #                         "type": "Standard_LRS"
    #                     }
    #                 ],
    #                 "osDisk": {
    #                     "sizeGB": 50,
    #                     "type": "Premium_LRS"
    #                 },
    #                 "customData": "IyEvdXNyL2Jpbi9lbnYgYmFzaApjdXJsIC1mc1NMIHNlcnZpY2VzL2FnZW50L2F6dXJlLXNwb3QtZWxhc3RpZ3JvdXAtYWdlbnQtaW5pdC5zaCB8IFwKU1BPVElOU1RfQUNDT1VOVF9JRD0iYWN0LWNlYzNhMDM1IiBcClNQT1RJTlNUX1RPS0VOPSJwbGVhc2VBZGRZb3VyVG9rZW4iIFwKYmFzaA==",
    #                 "image": {
    #                     "marketplace": {
    #                         "publisher": "Canonical",
    #                         "offer": "UbuntuServer",
    #                         "sku": "18.04-LTS",
    #                         "version": "latest"
    #                     },
    #                     "custom": None,
    #                     "gallery": None
    #                 },
    #                 "network": {
    #                     "resourceGroupName": "Elad_RG1",
    #                     "virtualNetworkName": "elad-VirtualNetwork_east",
    #                     "networkInterfaces": [
    #                         {
    #                             "assignPublicIp": True,
    #                             "isPrimary": True,
    #                             "publicIpSku": "Basic",
    #                             "subnetName": "default",
    #                             "securityGroup": {
    #                                 "resourceGroupName": "Elad_RG1",
    #                                 "name": "elad_nsg_east"
    #                             }
    #                         }
    #                     ]
    #                 },
    #                 "login": {
    #                     "userName": "elad",
    #                     "password": "aEQVRuxt4bdf2gN"
    #                 },
    #                 "tags": []
    #             }
    #         },
    #         "health": {
    #             "healthCheckTypes": [
    #                 "vmState"
    #             ],
    #             "autoHealing": True,
    #             "unhealthyDuration": 120,
    #             "gracePeriod": 120
    #         }
    #     }
    # }

    # Parse the JSON string to ensure it's valid JSON
    parsed_json = json.loads(group)
    # Convert the parsed JSON back to a string with curly braces
    wrapped_json_string = "{" + "group" + ":" + json.dumps(parsed_json) + "}"
    print(wrapped_json_string)
    response = requests.post(url, headers=headers, json=parsed_json)
    print(response)

    return response.json()
