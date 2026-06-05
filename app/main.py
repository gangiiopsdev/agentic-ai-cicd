from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {host}')
        subprocess.check_call(args, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

    return {'status': 'completed'}