from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['127.0.0.1', 'localhost']
    return any(host.startswith(safe) for safe in safe_hosts)

def safe_ping(host):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1'] + [host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}