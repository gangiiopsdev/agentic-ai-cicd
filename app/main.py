from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using shlex to escape command arguments
        subprocess.call(shlex.split(f"ping {host}"))
    except Exception as e:
        return {'error': str(e)}
    return {'status': 'completed'}