from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate IP address format
    if re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', host):
        # Safe implementation with input validation and sanitization
        if host.startswith('192.168.') or host.startswith('10.'):  # Example of allowed IP ranges
            subprocess.call(['ping', host])
    return {"status": "completed"}