from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Escape host input to prevent command injection
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)