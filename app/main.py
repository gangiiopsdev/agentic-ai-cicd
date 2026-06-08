from fastapi import FastAPI
import subprocess
def ping_safe(host: str):
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'denied', 'message': 'Unauthorized host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping_safe(host)