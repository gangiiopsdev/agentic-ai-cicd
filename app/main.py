from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'error': e.output}
    else:
        return {'error': 'Invalid host'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}