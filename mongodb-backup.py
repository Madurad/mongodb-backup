import subprocess
import shellx

#Add DB and the collection you want to backup
command = shlex.split("mongodump  --db incentivo-silverware-transactions --collection silverware-order-import-summary")

process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()
print output
