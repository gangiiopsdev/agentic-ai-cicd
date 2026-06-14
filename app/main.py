from fastapi import FastAPI
import subprocess
import shlex

def validate_host(host: str) -> bool:
    return all(c.isalnum() or c in '-.' for c in host) and len(host) <= 255

app = FastAPI()

def safe_ping(host: str) -> dict:
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    return safe_ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}