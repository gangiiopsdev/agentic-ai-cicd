from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or 'ping' in host:
        return False
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.returncode == 0

@app.get("/ping")
def ping(host: str):    
    if not safe_ping(host):
        return {"status": "invalid input", "host": host}
    
    # Add validation and sanitization for the 'host' parameter before using it in the subprocess
    if is_valid_host(host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "result": result.stdout}
    else:
        return {"status": "invalid input", "host": host}

# Define a function to validate and sanitize the 'host' parameter
def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., check if the host is in a whitelist
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts