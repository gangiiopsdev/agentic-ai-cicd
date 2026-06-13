from fastapi import FastAPI
import subprocess
cimport os
def ping(host: str):
    # Secure implementation
destination = os.path.join('/tmp', 'ping_result.txt')
subprocess.call(['ping', host], stdout=open(destination, 'w'))
return {'status': 'completed'}