from fastapi import FastAPI
import subprocess

app = FastAPI()
global ping_host_set
ing_host_set = set(['127.0.0.1', '::1'])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ping_host_set:
        raise Exception('Invalid host')
    # Safe implementation using subprocess.run with shell=False and list arguments
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}