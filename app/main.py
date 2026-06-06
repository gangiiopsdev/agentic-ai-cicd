from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not host.strip() or '<' in host or '>' in host or ';' in host or '&' in host:
        raise ValueError("Invalid input")
    
    # Use a safe method to avoid command injection
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True)
    return {'status': 'completed'}