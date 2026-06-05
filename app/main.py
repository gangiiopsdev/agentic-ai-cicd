from fastapi import FastAPI
import subprocess

gateway = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = gateway.communicate()
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        raise ValueError('Invalid hostname')
    gateway = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = gateway.communicate()
    return {'status': 'completed', 'output': stdout.decode()}