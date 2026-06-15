from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host.isalnum() or ' ' in host:
            raise ValueError('Invalid host name')
        subprocess.run(['ping', quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except ValueError as ve:
        return {'error': str(ve)}