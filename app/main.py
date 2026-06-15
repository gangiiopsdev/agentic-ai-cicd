from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host for ping')
    # Use shlex.quote to escape any special characters in the host input
    subprocess.run(['ping', '-c', '4', subprocess.list2cmdline([host])], check=True, text=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}