from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False
    if re.match(r'^\d{1,3}\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}$', host) and all(0 <= int(octet) <= 255 for octet in host.split('.')):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'invalid_host'}