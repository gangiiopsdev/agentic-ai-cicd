from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str):
    # Validate the host input using regex to allow only specific patterns (e.g., alphanumeric and hyphens)
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return "Invalid input"

    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return await safe_ping(host)