 #below code will list all VPC's which matches both Name Tag Value and the CIDR block:

import boto3

client = boto3.client('ec2',region_name='ap-south-1')
response = client.describe_vpcs(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'maven-vpc',
            ]
        },
        {
            'Name': 'cidr-block-association.cidr-block',
            'Values': [
                '172.63.0.0/24', #Enter you cidr block here
            ]
        },        
    ]
)
resp = response['Vpcs']
for i in resp:
    print(i["VpcId"])
