from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        raise ValueError("Invalid host input")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ["example.com", "test.com"]
    return host in allowed_hosts