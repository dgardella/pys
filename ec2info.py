#!/usr/bin/env python3
import boto3
import sys
from termcolor import colored


instanceid = sys.argv[1]

ec2 = boto3.resource('ec2', region_name='eu-west-1')
asg = boto3.client('autoscaling', region_name='eu-west-1')
#for instance in ec2.instances.all():
for instance in ec2.instances.filter(Filters=[{'Name': 'instance-id', 'Values': [instanceid]}]):
    print ()
    #print (colored(' ****  getting info of instance.id : ' , instance , '******** ', 'green'))
    print ("ID : ", instance.id)
    print ("STATE :", instance.state)
    print ("Public IP :", instance.public_ip_address)
    print ("Private IP :", instance.private_ip_address)
    print ("DNS Name :", instance.public_dns_name , "/" ,instance.private_dns_name)
    if instance.tags:
        print()
        print (" ------ labels ------- ")
        for tag in instance.tags:
            print ( tag['Key'] , " ---> " , tag['Value'] )
        print (" ------ ---- ------- ")
        print ()
    print ( "Checking if the instance belongs to an ASG .... ")
    all_asg = asg.describe_auto_scaling_groups()
    for asg_name in all_asg['AutoScalingGroups']:
        #print('ASG Name: ' + asg_name['AutoScalingGroupName'])
        for asg_ec2 in asg_name['Instances']:
            #print('Instance: ' + asg_ec2['InstanceId'])
            if asg_ec2['InstanceId'] == instance.id :
                print ("Yep :ASG_NAME --> " , asg_name['AutoScalingGroupName'])
    print ()
