from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host) or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}