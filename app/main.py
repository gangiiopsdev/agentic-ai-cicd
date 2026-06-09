from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters or paths
    if not re.match(r'^[a-zA-Z0-9]+$', host) or '..' in host:
        raise ValueError("Invalid host name")
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = await safe_ping(host)
    return {"status": "completed", "output": output}