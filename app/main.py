from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in '.-:' for c in host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    run_ping(host)
    return {'status': 'completed'}