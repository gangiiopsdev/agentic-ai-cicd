from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation using subprocess.run with a list of arguments instead of a single string.
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    ping_safe(host)
    return {"status": "completed"}