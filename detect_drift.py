import time
import boto3
client = boto3.client("cloudformation", region_name='eu-west-1')
stack = 'dsegura-tct-packaging-instance'
detection_id = client.detect_stack_drift(StackName=stack)
id6 = detection_id['StackDriftDetectionId']
#print (id6)
print ("------------")
time.sleep (3)
response = client.describe_stack_drift_detection_status(StackDriftDetectionId=detection_id['StackDriftDetectionId'])
#response = client.describe_stack_drift_detection_status(StackDriftDetectionId="0ec97ed0-acd1-11ea-9a6f-02abe6210ac8")
while response['DetectionStatus'] == "DETECTION_IN_PROGRESS":
    print ("Detection in progres")
    time.sleep(5)
    print ( "retrying" )

print (response['StackId'])
print (response['StackDriftStatus'])
print (response['DetectionStatus'])
    