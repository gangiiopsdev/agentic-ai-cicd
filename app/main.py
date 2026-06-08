from fastapi import FastAPI
import subprocess
global host_list
host_list = ['8.8.8.8', '127.0.0.1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in host_list:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}