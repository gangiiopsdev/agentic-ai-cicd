from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.strip() or not any(c.isalnum() for c in host) or len(host.split('.')) != 4:
        return False
    return True
app = FastAPI()
@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host format"}
    command = shlex.split(f'ping {host}')
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}