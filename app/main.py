from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = shlex.split(f'ping -c 1 {shlex.quote(host)}')
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Ping failed with error: {error.decode()}')

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '.' not in host:
        raise Exception(f'Invalid host: {host}')
    safe_ping(host)
    return {"status": "completed"}