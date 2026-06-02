from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host")
    return f'ping {host}'

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = safe_ping(host)
    result = subprocess.run(command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}