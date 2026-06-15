from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    return False

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if sanitize_host(host):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'unauthorized', 'message': 'Host not allowed'}, 403