from fastapi import FastAPI
import subprocess
global host_filter
host_filter = ["127.0.0.1", "localhost"]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in host_filter:
        return {"status": "error", "message": "Invalid host"}
    # Sanitize input to prevent command injection
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    
    return {"status": "completed"}