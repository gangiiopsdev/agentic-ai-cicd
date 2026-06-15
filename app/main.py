from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation, replace with more robust validation logic as needed
    allowed_hosts = ['example.com', '127.0.0.1']
    if host in allowed_hosts:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400