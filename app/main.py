from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    return 'ping', host

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command, arg = validate_host(host)
    result = subprocess.run([command, arg], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}