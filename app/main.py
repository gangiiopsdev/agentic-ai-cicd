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
        # Validate the input to prevent command injection
        if not all(c.isalnum() or c in ['-', '.'] for c in host):
            return {'error': 'Invalid hostname'}
        # Use shlex to safely quote arguments
        subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}