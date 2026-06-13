from fastapi import FastAPI
import subprocess
global_result = None

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        return {"error": "Invalid host input"}, 400
    global_result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": global_result.stdout}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if the host is a valid IP or domain name
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None