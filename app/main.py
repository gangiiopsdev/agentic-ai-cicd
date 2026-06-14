from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Fixed implementation using shlex to safely pass arguments
        subprocess.call(['ping'] + shlex.split(host))
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}