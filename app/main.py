from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host) or len(host) > 255:
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}