from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Add validation logic here (e.g., allow only certain IP ranges)
    return host == 'example.com'

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ["ping", host]
    # Use a whitelist for hosts to prevent arbitrary command execution
    subprocess.run(args, check=True)
    return {"status": "completed"}