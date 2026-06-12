from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate input to ensure it does not contain malicious commands
    if '&&' in host or ';' in host:
        raise ValueError('Invalid input')
    try:
        output = subprocess.check_output(shlex.split('ping ' + host), stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)