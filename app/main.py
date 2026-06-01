from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'stdout': result.stdout, 'stderr': result.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)