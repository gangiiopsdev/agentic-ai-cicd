from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-'))
    subprocess.run(['ping', quote(safe_host)], capture_output=True, text=True)
    return {'status': 'completed'}