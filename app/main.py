from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    # Add a more robust validation logic here, e.g., regex to allow only valid IP addresses or domain names
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.match(pattern, host) and subprocess.call(['ping', '-c', '1', '-C', '1', host], capture_output=True, text=True).returncode == 0:
        return True
    return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid host"}