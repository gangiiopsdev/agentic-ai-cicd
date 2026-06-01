from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

def validate_host(host):
    # Add validation logic here, e.g., allowed IP ranges or specific domain names
    if not host.isdigit():  # Simplified example for demonstration
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    safe_ping(host)
    return {"status": "completed"}