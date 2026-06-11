from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Simple validation: only allow alphanumeric characters and hyphens
    return all(c.isalnum() or c == '-' for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid host"}, 400
    command = ["ping", *shlex.split(host)]
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}