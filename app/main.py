from fastapi import FastAPI
import subprocess
import re
global ping_blacklist = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host not in ping_blacklist and re.match(r'^[a-zA-Z0-9.-]+$', host):
        subprocess.call(['ping', host])  # Using list for command arguments
    else:
        return {"status": "error", "message": "Invalid host"}

    return {"status": "completed"}