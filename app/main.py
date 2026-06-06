from fastapi import FastAPI
import subprocess
def safe_subprocess_call(command):
    try:
        subprocess.call(command)
    except Exception as e:
        raise ValueError(f'Command execution failed: {e}')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.strip().isalnum():
        raise ValueError('Invalid input')
    safe_subprocess_call(['ping', '-c', '4', host])  # Use absolute path for 'ping' and specify count
    return {'status': 'completed'}