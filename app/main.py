from fastapi import FastAPI
import subprocess

gitignore=['__pycache__', '*.log', '.env', 'venv']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Ensure host input is sanitized before passing to subprocess
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}

# Function to sanitize and validate host input
def validate_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts