from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _safe_ping(host: str) -> str:
    parts = shlex.split(host)
    if len(parts) != 1:
        raise ValueError('Invalid host format')
    return 'ping ' + parts[0]

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = _safe_ping(host)
        result = subprocess.run(safe_host, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}