from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate the host input to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    cmd = ['ping', *shlex.split(host)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)