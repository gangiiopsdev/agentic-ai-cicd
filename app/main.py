from fastapi import FastAPI
import subprocess
from shlex import quote
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
    return ''.join(char for char in input_str if char in allowed_chars)

def validate_host(host):
    # Add validation logic here, e.g., whitelist of allowed hosts
    allowed_hosts = ['localhost', '127.0.0.1']  # Example validation
    return host.strip() in allowed_hosts

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not validate_host(sanitize_input(host)):
        return JSONResponse(status_code=400, content={"status": "error", "message": "Invalid host"})
    args = ['ping', quote(host)]  # Use shlex.quote to escape special characters in the hostname
    result = subprocess.run(args, capture_output=True, text=True, check=True)  # Use check=True to raise an exception on error
    return JSONResponse(status_code=200, content={"status": "completed", "output": result.stdout})