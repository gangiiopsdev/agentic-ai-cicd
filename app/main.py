from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']  # Define allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):  # Validate the host before using it in subprocess
        command = ['ping'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True)
        return {
            "status": "completed",
            "output": result.stdout,
            "errors": result.stderr
        }
    else:
        return {"status": "error", "message": "Invalid host"}