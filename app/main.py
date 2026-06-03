from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host input')
    args = shlex.split(f'ping -c 1 {host}')
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Subprocess failed: {stderr.decode()}')
    return {"status": "completed", "output": stdout.decode()}