from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    safe_host = escape_host(host)
    args = ['ping', '--'] + [safe_host]  # Use -- to prevent injection
    subprocess.call(args)
    return {"status": "completed"}