from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input using regex to allow only specific patterns (e.g., alphanumeric and hyphens)
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return "Invalid input"

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)