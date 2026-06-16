from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = ''.join(filter(str.isalnum, host))  # Sanitize the input
    args = shlex.split(f'ping {safe_host}')
    subprocess.call(args)
    return {"status": "completed"}