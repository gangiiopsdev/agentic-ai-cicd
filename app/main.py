from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host: str) -> str:
    return shlex.quote(host)

def validate_host(host: str) -> bool:
    # Implement validation logic to ensure the host is safe
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {
            "status": "error",
            "message": "Invalid host"
        }
    escaped_host = escape_host(host)
    result = subprocess.run(["ping", "-c", str(4), escaped_host], check=True, capture_output=True, text=True, shell=False)
    return {
        "status": "completed",
        "response": result.stdout
    }