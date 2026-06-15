from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using shlex to avoid command injection
        subprocess.call(shlex.split(f'ping {host}'))
    except Exception as e:
        return {'error': str(e)}

    return {'status': 'completed'}