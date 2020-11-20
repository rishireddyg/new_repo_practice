import boto3
ec2_client = boto3.client('ec2')

print('All Security Groups:')
print('----------------')
sg_all = ec2_client.describe_security_groups()
for sg in sg_all['SecurityGroups'] :
    print(sg['GroupName'])


print('Subnets:')
print('-------')
sn_all = ec2_client.describe_subnets()
for sn in sn_all['Subnets'] :
    for tag in sn['Tags']:
        if tag['Key'] == 'Name':
            print(tag['Value'])