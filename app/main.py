from fastapi import FastAPI
import subprocess
import shlex
import re
def safe_ping(host):
    if not host.strip():
        return {'error': 'Invalid input'}
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host format'}
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed'}