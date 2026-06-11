from fastapi import FastAPI
import subprocess
import shlex
generics = ['8.8.8.8', '192.168.0.1'] # List of safe hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in generics:
        return {'error': 'Unauthorized host'}
    # Safe implementation using subprocess.run with shlex.quote to prevent shell injection
    safe_host = shlex.quote(host)
    result = subprocess.Popen(['ping', '-c', '1', safe_host], capture_output=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}