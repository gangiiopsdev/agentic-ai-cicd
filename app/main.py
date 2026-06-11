from fastapi import FastAPI
import subprocess
cimport = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = cimport.communicate()
if cimport.returncode != 0:
    return {'status': 'failed', 'error': error.decode('utf-8')}
return {'status': 'completed'}
def ensure_safe_host(host):
    allowed_hosts = ['example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
# Usage
host = 'example.com'
ensure_safe_host(host)