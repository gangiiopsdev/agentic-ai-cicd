from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> str:
    allowed_hosts = ['example.com']  # List of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    cmd = ['ping', '-c', '1', shlex.quote(host)]
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    return {'status': 'completed', 'output': output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return result
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}