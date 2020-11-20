import boto3
ec2 = boto3.resource('ec2')

ec2_demo= [{'Name':'instance-state-Name', 'Values': ['running']}]

#response = ec2.stop_instances(ec2_demo)
ec2.instances.filter(Filters=ec2_demo).stop()
print('response')
