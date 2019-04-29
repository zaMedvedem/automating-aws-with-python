# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:572100061294:handleLabelDetectionTopic:52590a9f-5bff-41e2-b7c7-274746cc9dd2', 'Sns': {'Type': 'Notification', 'MessageId': '4d03627d-1476-5a1e-935e-373c4ba5cb3c', 'TopicArn': 'arn:aws:sns:us-east-1:572100061294:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"5ec0c2b0f64d0d5c4ffdc1583f9d26a2411f37ced7bcf6adae92476823e4b337","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1556569491644,"Video":{"S3ObjectName":"Pexels Videos 4640.mp4","S3Bucket":"yevgenvideolyzervideos1223334444"}}', 'Timestamp': '2019-04-29T20:24:51.810Z', 'SignatureVersion': '1', 'Signature': 'mhCDr9jFMwVz+w8fKIqxc4ApOk6R92SK8ZjvvSygWj1sbiM4AJJc6Q5GdjkOUCGLcpM//Z1iZfVw2ATIs2ToTmXhjVh5GVjJnN1Ekypu4sld0hc/ypiW9QXwhz0zarxBhufSmsXcjQGwes0vFcfF4sQQFOwqa5NGMqfpP0Z7XLS0VV0A+9LrjYOMkpzAoOUEofsuTQPeQPKlz2Ucoa/FIJZxjzzD7Ps7SZrXOudGy0TCVSwa4jYSmxoQIKYkgFJ/JVQfYRRr3LR27V4vgdRXT7ifR1aV+eZ2qS/We9u2kFUSxUSqSmfOyMoUyuUQcWrmcVoVs2fDx7l/y4yorNfAXg==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:572100061294:handleLabelDetectionTopic:52590a9f-5bff-41e2-b7c7-274746cc9dd2', 'MessageAttributes': {}}}]}
event.keys()
event['Records'][0]
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['sns']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Message'][str(['JobId'])]
event['Records'][0]['Sns']['Message'][str('JobId')]
type(event['Records'][0]['Sns']['Message'])
import json
json.loads(event['Records'][0]['Sns']['Message'])
get_ipython().run_line_magic('save', 'handle-sns-event-example.py 1-99')
