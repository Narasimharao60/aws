import boto3

ec2 = boto3.resource('ec2')
res = ec2.instances.all()

for i in res:
    print({'id': i.id, 'name': i.tags[0]['Value'], 'state': i.state['Name']})

