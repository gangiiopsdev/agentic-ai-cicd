from fastapi import FastAPI
import subprocess
import shlex
g-import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.strip():
        raise ValueError("Host parameter cannot be empty")
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, shell=False)
    return {"status": "completed"}