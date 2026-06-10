from fastapi import FastAPI
import subprocess
import shlex

global_config = {
    "allowed_hosts": ["google.com", "example.com"]
}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in global_config['allowed_hosts']:
        subprocess.call(shlex.split(f'ping {host}'))
    else:
        return {"error": "Host not allowed"}
    return {"status": "completed"}