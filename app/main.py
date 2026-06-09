from fastapi import FastAPI
import subprocess
def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed characters and length
    return all(c.isalnum() or c in ('.', '-') for c in host) and len(host) > 0
def ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    return ping(host)