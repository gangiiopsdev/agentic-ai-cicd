from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # List of safe hosts
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    # Secure implementation using subprocess.run with shell=False and appropriate arguments
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}