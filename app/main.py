from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    allowed_hosts: List[str] = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host in allowed_hosts:
        command = ["ping", host]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        raise Exception("Invalid host")

# Preventive controls:
# - Use a whitelist of allowed hosts
# - Ensure proper input validation and sanitization
# - Consider using a library for network operations instead of subprocess