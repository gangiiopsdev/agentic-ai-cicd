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
        # Sanitize input to prevent command injection
        args = shlex.split(f'ping {shlex.quote(host)}')
        subprocess.call(args)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500