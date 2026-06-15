from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Using subprocess.run with shell=False for better control and safety
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input before using it
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host name'}
    return safe_ping(host)