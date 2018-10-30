import subprocess
import shlex
import boto3

def backup_db(mongodump):
    command = shlex.split(mongodump)
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, err = process.communicate()
        print output
        return True
    except:
        print ('An error occured during Backup of MongoDB')
        pass

def upload_to_s3(backupFile, s3Bucket, bucket_directory, file_format):
    s3 = boto3.resource('s3')
    try:
        s3.meta.client.upload_file(backupFile, s3Bucket, bucket_directory.format(file_format))
        return True
    except :
        print ('An error occured')
        pass

#Add DB and the collection you want to backup
if backup_db("mongodump  --db <dbName> --collection <collectionName> /path/to/backup/location/") is True:
    print ('Backup successfull')
    if upload_to_s3('/tmp/backup.py', 'bsfbackup', 'pfsense/{}', 'hello.py') is True:
        print ('Uploading to AWS S3  successfull')
else :
    print ('Failure Happend')
    


    


