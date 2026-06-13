from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        # Secure implementation using a full path to the executable and avoiding shell=True
        subprocess.call(['/usr/bin/ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400