from fastapi import FastAPI
import subprocess
guarded_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in guarded_hosts:
        raise ValueError('Unauthorized host')
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}