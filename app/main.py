from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str) -> str:
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    output = subprocess.check_output(args, stderr=subprocess.STDOUT)
    return output.decode()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result}
    except Exception as e:
        return {"status": "failed", "error": str(e)}