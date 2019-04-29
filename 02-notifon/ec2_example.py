# coding: utf-8
import boto3
session = boto3.Session(prifole_name='pythonAutomation')
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName_key_name)
key = ec2.create_key_pair(KeyName=key_name)
get_ipython().run_line_magic('clear', '')
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(ke.key_material)
    
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
    
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
ec2.images.filter(Owner=['amazon'])
list(ec2.images.filter(Owner=['amazon']))
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-922914f7')
img.name
ec2_apse2 = session.resource('ec2'. region_name='ap-southeast-2')
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-922914f7')
img_apse2.name
img,name
img.name
ami_name = img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20180508-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
filters
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_aspe2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
get_ipython().run_line_magic('clear', '')
img
key
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
ec2.Instance(id='i-0ccd9315d9f624363')
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
ssh -i python_automation_key.pem ec2-user@18.225.35.205
ssh -i python_automation_key.pem ec2-user@ec2-18-225-35-205.us-east-2.compute.amazonaws.com
ky_path
key_path
ssh -i python_automation_key.pem ec2-user@ec2-18-225-35-205.us-east-2.compute.amazonaws.com
ssh -i python_automation_key ec2-user@ec2-18-225-35-205.us-east-2.compute.amazonaws.com
ssh -i key_path ec2-user@ec2-18-225-35-205.us-east-2.compute.amazonaws.com
get_ipython().run_line_magic('clear', '')
inst.security_group
inst.security_groups
inst.security_groups[1]
sg = ec2.SecurityGroup('id')
sg = ec2.SecurityGroup('sg-ad2f87c1')
sg
sg = ec2.SecurityGroup(inst.ecurity_groups[0]['GroupId'])
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '162.249.177.117/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst
inst_public_dns_name
inst.public_dns_name
get_ipython().run_line_magic('history', '')
len(%history)
len(str(%history))
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('', 'save ec2_example.py')
get_ipython().run_line_magic('save', 'ec2_example.py')
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ec2_example.py')
get_ipython().run_line_magic('save', 'ec2_example.py 1..')
get_ipython().run_line_magic('save', 'ec2_example.py *')
get_ipython().run_line_magic('history', '-f ec2_example.py')
get_ipython().run_line_magic('save', 'ec2_example.py 1-9999')
