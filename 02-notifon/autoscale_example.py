# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = sessin.client('autoscaling')
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_clinet.describe_policies()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Down')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Down')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Down')
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'autoscale_example.py 1-99')
