from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use subprocess.run to avoid shell=True and command injection
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Ensure the 'host' parameter is sanitized before passing to subprocess
@app.get("/ping-sanitized")
def ping_sanitized(host: str):
    # Define a list of allowed hosts or use a whitelist/blacklist approach
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Host is not allowed"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}