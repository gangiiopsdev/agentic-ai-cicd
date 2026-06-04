from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['127.0.0.1', 'localhost']
    return any(host.startswith(safe) for safe in safe_hosts)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping'] + [host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}