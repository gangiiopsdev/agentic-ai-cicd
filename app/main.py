from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation to prevent common injection attacks
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'invalid host'}