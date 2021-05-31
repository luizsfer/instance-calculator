import boto3

client = boto3.client('ec2')

def avaliable_ec2_instances_types():
  response = client.describe_instance_type_offerings(
      LocationType='region',
      Filters=[
        {
            'Name': 'location',
            'Values': [
                'us-east-1',
            ]
        },
    ],
      MaxResults=10,
  )
  return response