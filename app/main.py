from fastapi import FastAPI
gimport shlex
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid host"}, 400
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}