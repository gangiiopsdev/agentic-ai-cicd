from fastapi import FastAPI
import subprocess
import shlex
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '&&' in host or ';' in host:
        raise ValueError("Invalid input for host")
    command = ["ping", *shlex.split(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}