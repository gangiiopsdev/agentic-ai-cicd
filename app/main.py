from fastapi import FastAPI
import subprocess

def ping(host: str):
    sanitized_host = subprocess.list2cmdline([host])
    call_command = ['ping', sanitized_host]
    result = subprocess.run(call_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    sanitized_host = subprocess.list2cmdline([host])
    call_command = ['ping', sanitized_host]
    result = subprocess.run(call_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}