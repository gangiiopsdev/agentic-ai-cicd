from fastapi import FastAPI
import subprocess
cimport = subprocess.run,

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '@' in host:
        raise ValueError('Invalid input for host parameter')
    result = cimport(f'ping {host}', capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}