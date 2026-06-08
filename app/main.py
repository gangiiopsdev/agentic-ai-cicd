from fastapi import FastAPI
import subprocess
import shlex

gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the host input to prevent command injection
        if not all(c.isalnum() or c in ('.', '-') for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True, input=None)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

    return {'status': 'completed'}