from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: f'ping {shlex.quote(host)} -c 1'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    subprocess.call(generate_ping_command(host), shell=False)
    return {"status": "completed"}