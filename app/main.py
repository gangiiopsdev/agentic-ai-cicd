from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate the host parameter
    if not host or ' ' in host or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get="/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"status": "error", "message": str(e)}