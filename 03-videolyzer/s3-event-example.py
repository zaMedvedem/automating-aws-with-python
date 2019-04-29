# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2019-04-29T18:08:19.822Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDAYKM6SFBXNVRUHNTVG'}, 'requestParameters': {'sourceIPAddress': '162.249.177.117'}, 'responseElements': {'x-amz-request-id': 'B5FFAACB59DBC77D', 'x-amz-id-2': '0VT5x67uQM8N++np23MGYGdnVkp6M/+uZXZg/iCWPsf0u30ciwMh9OxuGaeqbt5YrXXZzwF7tAQ='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '114f2710-fe9c-44c8-83ff-e1d511e65a66', 'bucket': {'name': 'yevgenvideolyzervideos1223334444', 'ownerIdentity': {'principalId': 'ADEGZN3B0Y9FO'}, 'arn': 'arn:aws:s3:::yevgenvideolyzervideos1223334444'}, 'object': {'key': 'Pexels+Videos+1093667.mp4', 'size': 7844922, 'eTag': '268675c9d03bf12a916ff2ca4be51ff2', 'sequencer': '005CC73D8837138E70'}}}]}
event
event['Records'][0]
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
