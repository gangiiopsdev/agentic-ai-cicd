from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return "Invalid host name"
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if isinstance(output, str) and 'Invalid host name' in output:
        return {"status": "error", "message": output}
    else:
        return {"status": "completed", "output": output}