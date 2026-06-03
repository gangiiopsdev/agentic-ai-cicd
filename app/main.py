from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def secure_ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call for better control and security
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Add validation to ensure host is alphanumeric or sanitized as needed
        return {"error": "Invalid input"}
    return secure_ping(host)