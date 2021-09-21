import boto3                                                                           
import os
import io
from datetime import datetime, timedelta

client = boto3.client('rds')

dbid = 'jhervas-tst-rds-04'       #set db identifier

log_file_name = 'error/mysql-error.log'
log_file_ec2 = './rds.log'

response = client.download_db_log_file_portion(DBInstanceIdentifier=dbid,   LogFileName=log_file_name)    #main API request to get the last log
buf = io.StringIO(response['LogFileData'])                                              #IO module to properly process log data

with open(log_file_ec2, 'w+') as tmp_file:                                                   #write everything to primary log
    tmp_file.write(buf.read())