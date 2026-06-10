from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', ':'] for c in host):
        raise ValueError('Invalid hostname')
    # Use shlex.quote to safely escape user input
    safe_host = shlex.quote(host)
    subprocess.run(['ping', '-c', '4', safe_host], check=True)
    return {'status': 'completed'}