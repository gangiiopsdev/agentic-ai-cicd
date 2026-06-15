from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    # Secure implementation
    subprocess.call(['ping', host])

    return {'status': 'completed'}