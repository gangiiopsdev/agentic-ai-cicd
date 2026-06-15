from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Sanitize the input to prevent command injection
    if any(char in host for char in ['&', '|', ';', '&&', '||']):
        raise ValueError('Invalid host input')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    execute_ping(host)
    return {'status': 'completed'}