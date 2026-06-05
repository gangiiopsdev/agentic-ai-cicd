from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add your validation logic here
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Safe implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}