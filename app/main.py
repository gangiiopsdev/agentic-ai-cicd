from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize input
        if not host or not host.isalnum():
            raise ValueError("Invalid hostname")
        result = subprocess.run(['ping', *shlex.quote(host).split()], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}