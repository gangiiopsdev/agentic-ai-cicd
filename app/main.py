from fastapi import FastAPI
import subprocess
from shlex import quote
def ping(host: str):
    sanitized_host = quote(host)
    call_command = ['ping', sanitized_host]
    result = subprocess.run(call_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    sanitized_host = quote(host)
    call_command = ['ping', sanitized_host]
    result = subprocess.run(call_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}