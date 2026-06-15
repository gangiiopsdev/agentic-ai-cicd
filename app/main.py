from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Validate the host input
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
def validate_host(host: str) -> bool:
    # Implement validation logic here (e.g., check for valid IP address or hostname format)
    return True
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return run_ping(host)