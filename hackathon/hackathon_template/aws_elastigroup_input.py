# Parse the input AWS Elastigroup JSON configuration
import json

aws_elastigroup_json = '''
{
    "group": {
        "name": "hackathon",
        "region": "us-east-1",
        "capacity": {
            "minimum": 1,
            "maximum": 10,
            "target": 5,
            "unit": "instance"
        },
        "strategy": {
            "availabilityVsCost": "balanced",
            "drainingTimeout": 120,
            "onDemandCount": 0,
            "fallbackToOd": true,
            "revertToSpot": {
                "performAt": "always"
            }
        },
        "compute": {
            "instanceTypes": {
                "ondemand": "t3.micro",
                "spot": [
                    "t2.micro",
                    "t2.small",
                    "t3.micro",
                    "c5.large",
                    "c5.4xlarge",
                    "r5.large",
                    "r5.4xlarge",
                    "m5.large",
                    "m5.4xlarge"
                ]
            },
            "availabilityZones": [
                {
                    "name": "us-east-1a",
                    "subnetIds": ["subnet-f0435e97"]
                }
            ],
            "launchSpecification": {
                "securityGroupIds": ["sg-009745adf0036dd94"],
                "monitoring": false,
                "imageId": "ami-05e91df996f6c7ffa"
            },
            "product" : "Linux/UNIX"
        },
        "scaling": {},
        "scheduling": {}
    }
}
'''