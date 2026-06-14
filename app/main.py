from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "error", "message": "Invalid host"}
    # Safe implementation using subprocess.run with shell=False and args parameter
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}