from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple validation logic (e.g., allow only alphanumeric characters)
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host parameter")
    subprocess.call(['ping', host])
    return {"status": "completed"}