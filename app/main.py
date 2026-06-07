from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Stronger regex to validate host input
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        return {"error": "Invalid host input"}
    # Safer implementation using subprocess.run with shell=False and properly formatted arguments
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}