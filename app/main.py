from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use safe implementation
    if not validate_host(host):
        raise ValueError("Invalid host name")
    output = safe_ping(host)
    return {"status": "completed", "output": output}

# Add a function to validate the host input
import re
def validate_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    if re.match(pattern, host):
        return True
    return False