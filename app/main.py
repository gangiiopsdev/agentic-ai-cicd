from fastapi import FastAPI
import subprocess
cimport = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = p.communicate()
if error:
    raise Exception('Ping failed: ' + str(error))
return {'status': 'completed'}