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
    if not host.isalnum() or '-' not in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    command = ['ping', *shlex.split(host)]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

    return {'status': 'completed'}