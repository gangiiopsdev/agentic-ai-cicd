from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    # Validate the host input
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Add your validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts