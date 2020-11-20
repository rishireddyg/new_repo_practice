import boto3
s3_obj=boto3.resource('s3')
for bucket in s3_obj.buckets.all():
    print (bucket)