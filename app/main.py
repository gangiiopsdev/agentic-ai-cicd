from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = ['ping', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = host.strip().replace(' ', '')  # Remove spaces and extra characters
    if not safe_host.isalnum() or len(safe_host) > 255:
        return {'status': 'error', 'output': 'Invalid input'}
    return safe_ping(safe_host)