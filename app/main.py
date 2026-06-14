from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> str:
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    output = subprocess.run(args, check=True, capture_output=True, text=True)
    return output.stdout

def safe_ping_host(host: str) -> str:
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    cmd = ["ping", host]
    output = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return output.stdout

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping_host(host)
        return {"status": "completed", "output": result}
    except Exception as e:
        return {"status": "failed", "error": str(e)}