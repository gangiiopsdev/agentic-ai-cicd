from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return False
    return True

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        # Secure implementation
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'denied', 'message': 'Invalid host'}, 403