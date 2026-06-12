from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', str(4), host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}