from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    cmd = ['ping', shlex.quote(host)]
    return subprocess.run(cmd)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'returncode': result.returncode}