from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Validate host input to prevent command injection
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            raise ValueError('Invalid host name')
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)