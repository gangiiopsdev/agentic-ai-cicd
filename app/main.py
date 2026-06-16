from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    # Fixed implementation using subprocess.run with shell=False and avoiding f-strings for arguments
    result = subprocess.call(['ping', '-c', '1', host])
    return result

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"status": "error", "message": str(e)}