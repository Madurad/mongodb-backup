import subprocess
import shlex

#Add DB and the collection you want to backup
command = shlex.split("mongodump  --db <dbName> --collection <collectionName> /path/to/backup/location/")

process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()
print output
