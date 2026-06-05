from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping', '-c', '4', host]
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not any(c in host for c in [';', '|', '&', '`', '$']):  # Basic check to prevent shell injection
        return safe_ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid input'}