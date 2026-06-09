from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Add your validation logic here, e.g., checking if the host is a valid IP address or hostname
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return pattern.match(host) is not None