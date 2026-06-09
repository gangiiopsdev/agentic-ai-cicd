from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Validate and sanitize the host input
    if not host.isalnum():
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command = shlex.split(f'ping {host}')
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}