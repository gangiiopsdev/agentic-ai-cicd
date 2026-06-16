from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip() and all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        command = shlex.split(f'ping {host}')
        subprocess.run(command, check=True)
    else:
        raise ValueError('Invalid host provided')
    return {"status": "completed"}