import boto3
ec2 = boto3.resource('ec2', region_name='ap-south-1')
volumes = ec2.volumes.all() # If you want to list out all volumes
volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['notin-use']}]) # if you want to list out only attached volumes
[volume for volume in volumes]
for v in volumes:
    print (v.id)