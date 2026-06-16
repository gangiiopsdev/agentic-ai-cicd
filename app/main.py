from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    # Basic regex to allow only alphanumeric characters, hyphens, and periods
    pattern = r'^[a-zA-Z0-9-.]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid hostname provided"}