from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent shell injection
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    response = safe_ping(host)
    return {"status": "completed", "response": response}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex check
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None