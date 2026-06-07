from fastapi import FastAPI, HTTPException
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters (e.g., alphanumeric and hyphen)
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")

    # Use a whitelist of allowed hosts or use a safer method to execute the ping command
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail="Access denied")

    result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}