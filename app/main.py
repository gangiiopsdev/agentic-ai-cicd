from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not validate_host(host):
        raise ValueError("Invalid host")
    
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }

def validate_host(host: str) -> bool:
    # Simple validation to ensure the host contains only alphanumeric characters and hyphens
    import re
    return re.match(r'^[a-zA-Z0-9-]+$', host) is not None

@app.get("/ping")
def ping(host: str):
    try:
        return secure_ping(host)
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "output": e.stdout,
            "error": e.stderr
        }