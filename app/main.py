from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)

def is_valid_host(host: str) -> bool:
    # Add validation logic here
    return '.' in host and len(host.split('.')) == 4

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}