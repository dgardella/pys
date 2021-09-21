import boto3
import pprint
import json
iam = boto3.client('iam')
response = iam.get_server_certificate(ServerCertificateName='BQ_20200622')
print(response['ServerCertificate'])
cert = json.dumps(response['ServerCertificate'])
print(cert)
