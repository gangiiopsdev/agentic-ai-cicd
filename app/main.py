from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using a whitelisted set of hosts
    allowed_hosts = {'example.com', 'test.com'}
    if host in allowed_hosts:
        sanitized_host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}