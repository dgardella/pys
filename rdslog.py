import boto3

token='0'
client = boto3.client('rds')

response = client.download_db_log_file_portion(
    DBInstanceIdentifier='jhervas-tst-rds-04',
    LogFileName='error/mysql-error.log',
    Marker=token,
    )

print (response)
