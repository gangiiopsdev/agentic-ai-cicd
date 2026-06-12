from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic for the host input
    return all(c.isalnum() or c in [".", "-"] for c in host)