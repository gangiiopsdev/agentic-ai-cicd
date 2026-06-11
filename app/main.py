from fastapi import FastAPI
import subprocess
global_hosts = ['127.0.0.1', '8.8.8.8']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_hosts:
        subprocess.call(['ping', '-c 1', host])  # Limit the number of pings to prevent DoS
    else:
        return {'status': 'invalid host', 'error': 'Host not allowed'}
    return {'status': 'completed'}