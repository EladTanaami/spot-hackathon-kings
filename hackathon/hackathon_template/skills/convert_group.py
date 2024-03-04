import json

def skill(aws_group, password, userName):
    elastigroup_parser = ElastigroupConverter(aws_group, password, userName)
    azure_elastigroup_json = elastigroup_parser.convert()

    return azure_elastigroup_json


class ElastigroupConverter:
    def __init__(self, aws_group, password, user_name):
        print(aws_group)
        self.aws_elastigroup_config = json.loads(aws_group)
        self.password = password;
        self.user_name = user_name;

    """
    Method defines the mapping from AWS regions to Azure regions
    """

    @staticmethod
    def from_aws_to_azure_images(aws_image):
        image_mapping = {
            "ami-0c94855ba95c71c99": {
                "marketplace": {
                    "publisher": "Canonical",
                    "offer": "UbuntuServer",
                    "sku": "18.04-LTS",
                    "version": "latest"
                }
            },
            "ami-0885b1f6bd170450c": {
                "marketplace": {
                    "publisher": "Amazon",
                    "offer": "AmazonLinux2",
                    "sku": "2.0",
                    "version": "latest"
                }
            },
            "ami-0d5d9d301c853a04a": {
                "marketplace": {
                    "publisher": "MicrosoftSQLServer",
                    "offer": "SQL2019-WS2019",
                    "sku": "Standard",
                    "version": "15.0"
                }
            },
            "ami-0a313d6098716f372": {
                "marketplace": {
                    "publisher": "Bitnami",
                    "offer": "WordPress",
                    "sku": "5.8",
                    "version": "latest"
                }
            },
            "ami-0d8f6eb4f641ef691": {
                "marketplace": {
                    "publisher": "RedHat",
                    "offer": "RHEL",
                    "sku": "8.4",
                    "version": "latest"
                }
            },
            "ami-0b6f6d3b7bbfd8b8c": {
                "marketplace": {
                    "publisher": "SUSE",
                    "offer": "SLES",
                    "sku": "15-SP3",
                    "version": "latest"
                }
            },
            "ami-0f9ae750e8274075b": {
                "marketplace": {
                    "publisher": "VMware",
                    "offer": "VMwareCloud",
                    "sku": "17.1",
                    "version": "latest"
                }
            },
            "ami-0c6b1d09930fac512": {
                "marketplace": {
                    "publisher": "Adobe",
                    "offer": "ColdFusion",
                    "sku": "2021",
                    "version": "latest"
                }
            },
            "ami-0f0cfd7e2c9e6c7b6": {
                "marketplace": {
                    "publisher": "Oracle",
                    "offer": "OracleLinux",
                    "sku": "8.4",
                    "version": "latest"
                }
            },
            "ami-0f7f9e2f840f6c6a8": {
                "marketplace": {
                    "publisher": "Couchbase",
                    "offer": "CouchbaseServer",
                    "sku": "7.0",
                    "version": "latest"
                }
            },
            "ami-0b1e14a0a0e0a8f6b": {
                "marketplace": {
                    "publisher": "MongoDB",
                    "offer": "MongoDBCommunity",
                    "sku": "5.0",
                    "version": "latest"
                }
            },
            "ami-0e2e3d4f5f6f7f8f9": {
                "marketplace": {
                    "publisher": "Cloudera",
                    "offer": "ClouderaDataPlatform",
                    "sku": "7.2",
                    "version": "latest"
                }
            },
            "ami-0a1b2c3d4e5f6g7h8": {
                "marketplace": {
                    "publisher": "IBM",
                    "offer": "IBMCloudPak",
                    "sku": "4.3",
                    "version": "latest"
                }
            },
            "ami-0i9u8y7t6r5e4w3q2": {
                "marketplace": {
                    "publisher": "Juniper",
                    "offer": "Junos",
                    "sku": "20.4",
                    "version": "latest"
                }
            },
            "ami-0z1x2c3v4b5n6m7q8": {
                "marketplace": {
                    "publisher": "Cisco",
                    "offer": "IOS-XRv9000",
                    "sku": "7.3",
                    "version": "latest"
                }
            },
            "ami-0p9o8i7u6y5t4r3e2": {
                "marketplace": {
                    "publisher": "PaloAltoNetworks",
                    "offer": "VM-Series",
                    "sku": "10.0",
                    "version": "latest"
                }
            },
            "ami-0s9d8f7g6h5j4k3l2": {
                "marketplace": {
                    "publisher": "Fortinet",
                    "offer": "FortiGate",
                    "sku": "7.0",
                    "version": "latest"
                }
            },
            "ami-0b1e2d3c4b5a6b7c8": {
                "marketplace": {
                    "publisher": "Citrix",
                    "offer": "CitrixADC",
                    "sku": "13.0",
                    "version": "latest"
                }
            },
            "ami-0x1y2z3a4b5c6d7e8": {
                "marketplace": {
                    "publisher": "Splunk",
                    "offer": "SplunkEnterprise",
                    "sku": "8.2",
                    "version": "latest"
                }
            },
            "ami-0a9b8c7d6e5f4g3h2": {
                "marketplace": {
                    "publisher": "TrendMicro",
                    "offer": "DeepSecurity",
                    "sku": "12.0",
                    "version": "latest"
                }
            },
            "ami-0c55b159cbfafe1f0": {
                "publisher": "Canonical",
                "offer": "UbuntuServer",
                "sku": "16.04-LTS",
                "version": "latest"
            },
            "ami-0c94855ba95c71c99": {
                "marketplace": {
                    "publisher": "Microsoft",
                    "offer": "WindowsServer",
                    "sku": "2019-Datacenter",
                    "version": "latest"
                }
            },
            "ami-0d5d9d301c853a04a": {
                "marketplace": {
                    "publisher": "Microsoft",
                    "offer": "WindowsServer",
                    "sku": "2019-Datacenter",
                    "version": "latest"
                }
            },
            "ami-06f2f7794649bdc1e": {
                "marketplace": {
                    "publisher": "Microsoft",
                    "offer": "WindowsServer",
                    "sku": "2016-Datacenter",
                    "version": "latest"
                }
            },
            "ami-0a313d6098716f372": {
                "marketplace": {
                    "publisher": "Microsoft",
                    "offer": "WindowsServer",
                    "sku": "2016-Datacenter",
                    "version": "latest"
                }
            },
            "ami-0d8f6eb4f641ef691": {
                "marketplace": {
                    "publisher": "Microsoft",
                    "offer": "WindowsServer",
                    "sku": "2012-R2-Datacenter",
                    "version": "latest"
                }
            },
            "ami-0b6f6d3b7bbfd8b8c": {
                "marketplace": {
                    "publisher": "Microsoft",
                    "offer": "WindowsServer",
                    "sku": "2012-R2-Datacenter",
                    "version": "latest"
                }
            }
        }

        print("here5")
        return image_mapping.get(aws_image, {"Unknown": "Unknown"})

    @staticmethod
    def from_aws_to_azure_region(aws_region):
        region_mapping = {
            "us-east-1": "eastus",
            "us-west-1": "westus",
            "us-west-2": "westus2",
            "eu-west-1": "westeurope",
            "eu-west-2": "uksouth",
            "eu-central-1": "northeurope",
            "ap-southeast-1": "southeastasia",
            "ap-southeast-2": "australiaeast",
            "ap-northeast-1": "japaneast",
            "ap-northeast-2": "japanwest",
            "sa-east-1": "brazilsouth",
            "ca-central-1": "canadacentral",
            "ap-south-1": "centralindia",
            "us-gov-west-1": "usgovvirginia",
            "us-gov-east-1": "usgovarizona",
            "af-south-1": "southafricanorth",
            "me-south-1": "uaecentral",
            "eu-south-1": "francecentral",
            "eu-north-1": "norwayeast",
            "ap-east-1": "hongkong",
            # Add more region mappings as needed
        }

        print("here2")
        return region_mapping.get(aws_region, "Unknown")

    @staticmethod
    def from_aws_to_azure_instance_type(aws_instance_types):
        instance_type_mapping = {
            # General purpose
            't2.micro': 'Standard_A1_v2',
            't2.small': 'Standard_A1_v2',
            't3.micro': 'Standard_A1_v2',
            't3.small': 'Standard_A2_v2',
            # Compute optimized
            'c5.large': 'Standard_F2s_v2',
            'c5.xlarge': 'Standard_F4s_v2',
            'c5.2xlarge': 'Standard_F8s_v2',
            'c5.4xlarge': 'Standard_F16s_v2',
            # Memory optimized
            'r5.large': 'Standard_E2s_v3',
            'r5.xlarge': 'Standard_E4s_v3',
            'r5.2xlarge': 'Standard_E8s_v3',
            'r5.4xlarge': 'Standard_E16s_v3',
            # Balanced CPU-to-memory ratio
            'm5.large': 'Standard_D2s_v3',
            'm5.xlarge': 'Standard_D4s_v3',
            'm5.2xlarge': 'Standard_D8s_v3',
            'm5.4xlarge': 'Standard_D16s_v3',
            # Storage optimized
            'i3.large': 'Standard_L4s',
            'i3.xlarge': 'Standard_L8s',
            'i3.2xlarge': 'Standard_L16s',
            'i3.4xlarge': 'Standard_L32s',
            # GPU instances
            'p3.2xlarge': 'Standard_NC6s_v3',
            'p3.8xlarge': 'Standard_NC24s_v3',
            'p3.16xlarge': 'Standard_NC24rs_v3',
            # High performance computing
            'h1.2xlarge': 'Standard_H16rs',
            'h1.4xlarge': 'Standard_H32rs',
            'h1.8xlarge': 'Standard_H64rs',
            'h1.16xlarge': 'Standard_H128rs',
            # FPGA instances
            'f1.2xlarge': 'Standard_F2s',
            'f1.4xlarge': 'Standard_F4s',
            'f1.16xlarge': 'Standard_F16s',
            # Add more instance type mappings as needed
        }

        print("here3")
        azure_vm_sizes = [instance_type_mapping.get(it, None) for it in aws_instance_types]
        return list(filter(None, azure_vm_sizes))

    """
    Method defines the mapping from AWS instance types to Azure VM Sizes
    """

    """
    Method defines the mapping from AWS strategy to Azure strategy
    """

    @staticmethod
    def from_aws_to_azure_strategy(aws_strategy):
        # If aws strategy availabilityVsCost is balanced then 50, if it is cheapest then 0, else then 100
        if aws_strategy['availabilityVsCost'] == "balanced":
            strategy = 50
        elif aws_strategy['availabilityVsCost'] == "cheapest":
            strategy = 0
        else:
            strategy = 100

        print("here4")
        # This is a simplified example, you will need to adjust the mapping based on actual strategy options
        azure_strategy = {
            'availabilityVsCost': 50 if aws_strategy['availabilityVsCost'] == "balanced" else 0 if aws_strategy[
                                                                                                       'availabilityVsCost'] == "cheapest" else 100,
            'onDemandCount': aws_strategy.get('onDemandCount', 0),
            'drainingTimeout': aws_strategy.get('drainingTimeout', None),
            'fallbackToOd': aws_strategy.get('fallbackToOd', None)
        }
        return azure_strategy

    """
    Method defines the mapping from AWS compute to Azure compute
    """

    def map_compute(self, aws_compute):
        azure_compute = {
            #changed it to hardcoded
            'os': 'Linux',
            'vmSizes': {
                'odSizes': ElastigroupConverter.from_aws_to_azure_instance_type(
                    [aws_compute['instanceTypes']['ondemand']]),
                'spotSizes': ElastigroupConverter.from_aws_to_azure_instance_type(aws_compute['instanceTypes']['spot'])
            },
            'launchSpecification': {
                'image': {
                    "marketplace": {
                        "publisher": "Canonical",
                        "offer": "UbuntuServer",
                        "sku": "18.04-LTS",
                        "version": "latest"
                    },
                },
                'network': {
                    'resourceGroupName': 'Elad_RG1',
                    'virtualNetworkName': 'elad-VirtualNetwork_east',
                    'networkInterfaces': [
                        {
                            'assignPublicIp': True,
                            'isPrimary': True,
                            'publicIpSku': 'Standard',
                            'subnetName': 'default',
                            'securityGroup': {
                                'resourceGroupName': 'Elad_RG1',
                                'name': 'elad_nsg_east'
                            }
                        }
                    ]
                },
                'login': {
                    'userName': self.user_name,
                    'password': self.password
                }
            }
        }

        return azure_compute

    """
    Method converts aws elastigroup config to azure elastigroup config json
    """

    def from_aws_to_azure_group_config(self, aws_elastigroup_config):
        return {
            'group': {
                'name': aws_elastigroup_config.get('name', None),
                'region': self.from_aws_to_azure_region(aws_elastigroup_config.get('region', None)),
                'resourceGroupName': 'Elad_RG1',  # todo need to create in azure
                'capacity': {
                    'minimum': self.aws_elastigroup_config['capacity'].get('minimum', None),
                    'maximum': self.aws_elastigroup_config['capacity'].get('maximum', None),
                    'target': self.aws_elastigroup_config['capacity'].get('target', None)
                },
                'strategy': self.from_aws_to_azure_strategy(aws_elastigroup_config['strategy']),
                'compute': self.map_compute(aws_elastigroup_config['compute']),
                # Azure might have different configurations for scaling and scheduling
                'scaling': None,
                'scheduling': None
            }
        }

    """
    Convert an Elastigroup config from an Azure to an AWS Resource
    """

    def convert(self):
        return json.dumps(self.from_aws_to_azure_group_config(aws_elastigroup_config=self.aws_elastigroup_config))
