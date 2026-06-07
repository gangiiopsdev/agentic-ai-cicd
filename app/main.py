from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    if not host:
        return {'status': 'Invalid host'}
    if '.' in host or ':' in host or '\' in host:
        return {'status': 'Invalid host'}
    subprocess.run(['ping', quote(host)], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host:
        return {'status': 'Invalid host'}
    if '.' in host or ':' in host or '\' in host:
        return {'status': 'Invalid host'}
    subprocess.run(['ping', quote(host)], check=True)
    return {"status": "completed"}