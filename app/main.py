from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input using shlex.quote to prevent shell injection
    safe_host = shlex.quote(host)
    try:
        result = subprocess.check_output(['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': result.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}