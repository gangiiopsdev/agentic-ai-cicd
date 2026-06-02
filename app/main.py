from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    try:
        # Use a whitelist of allowed hosts or validate the host more strictly
        if not host.isalnum() or '.' in host:
            raise ValueError('Invalid hostname')
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)