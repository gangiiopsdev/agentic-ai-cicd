from fastapi import FastAPI
import subprocess
import re
def validate_host(host):
    allowed_hosts = ['example.com', '192.168.1.1']  # Replace with actual validation logic
    if host not in allowed_hosts:
        raise ValueError('Invalid host input')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', shlex.quote(host)]  # Use shlex.quote to escape special characters
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}