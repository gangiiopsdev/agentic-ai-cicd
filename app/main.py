from fastapi import FastAPI
import subprocess
import shlex
def safe_getinput(command):
    return subprocess.run(shlex.split(command), capture_output=True, text=True).stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        return {"status": "error", "result": "Invalid host"}
    result = safe_getinput(f'ping -c 4 {host}')
    return {"status": "completed", "result": result}
def validate_host(host: str) -> bool:
    # Add validation logic to ensure the host is safe
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts