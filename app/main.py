from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not validate_host(host):
        raise ValueError("Invalid host")
    return execute_ping(host)

def validate_host(host: str) -> bool:
    # Simple validation, replace with more comprehensive checks as needed
    allowed_hosts = ["127.0.0.1", "example.com"]
    return host in allowed_hosts