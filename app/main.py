from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    parts = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(parts, capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)