from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def sanitize_host(host):
    # Implement host sanitization logic here
    return host.replace(';', '').replace('|', '')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command_parts = ['ping', sanitized_host]
    subprocess.run(command_parts, check=True)
    return {'status': 'completed'}