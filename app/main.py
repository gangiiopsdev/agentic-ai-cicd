from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None and re.match(r'^(([1-9]|[1-9][0-9]|1[0-9]{2}|2([0-4][0-9]|5[0-5]))\.){3}([1-9]|[1-9][0-9]|1[0-9]{2}|2([0-4][0-9]|5[0-5]))$', host) is not None

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Add additional checks to ensure the host is a valid IP address or hostname