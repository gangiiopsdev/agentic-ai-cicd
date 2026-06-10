from fastapi import FastAPI
import subprocess
cimport = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = cimport.communicate()
if cimport.returncode != 0:
    return {'status': 'failed', 'error': error.decode('utf-8')}
return {'status': 'completed'}