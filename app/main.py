from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Sanitize and validate the host input before executing the command
    if not isinstance(host, str) or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    # Use a whitelist of allowed hosts or use an alternative method for pinging
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}