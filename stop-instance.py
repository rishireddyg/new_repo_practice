import boto3

ec2_client = boto3.resource('ec2')

instances = ec2_client.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running','stopped']}])
for instance in instances:
    print(instance.id, instance.instance_type)
ec2_filter= [{'Name': 'instance-state-name', 'Values': ['running']}]

ec2_client.instances.filter(Filters=ec2_filter).stop()

print('Subnets:')
print('-------')
#sn_all = ec2.describe_subnets()
#for sn in sn_all['Subnets'] :
#    print(sn['SubnetName'])


print('All Security Groups:')
print('----------------')
sg_all = ec2_client.describe_security_groups()
for sg in sg_all['SecurityGroups'] :
    print(sg['GroupName'])