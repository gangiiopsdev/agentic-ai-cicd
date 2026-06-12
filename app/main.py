from fastapi import FastAPI
import subprocess
import shlex
c
app = FastAPI()

def validate_host(host):
    allowed_hosts = ['host1', 'host2']  # Define a list of allowed hosts
    return host in allowed_hosts

def sanitize_host(host):
    sanitized_host = ''.join(e for e in host if e.isalnum() or e in '-.')  # Basic sanitization
    return sanitized_host

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=403, detail="Invalid host")
    sanitized_host = sanitize_host(host)
    # Secure implementation
    subprocess.call(shlex.split(f"ping {sanitized_host}"))
    return {"status": "completed"}