from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)
def validate_host(host):
    # Add validation logic here to ensure the host is safe
    return True