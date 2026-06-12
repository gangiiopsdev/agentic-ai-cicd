from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Add validation logic here, e.g., allowed hosts list
    allowed_hosts = ['example.com', 'localhost']
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
        args = ['ping', host]
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        return {'status': 'invalid host'}, 400