from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or not host.strip():
        raise ValueError('Host parameter is required and cannot be empty')
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": result.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}