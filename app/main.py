from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to prevent shell injection
        if not host.isalnum() and not '.' in host and not '-' in host:
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except ValueError as ve:
        return {'error': str(ve)}