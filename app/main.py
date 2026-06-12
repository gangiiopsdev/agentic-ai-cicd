from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not is_valid_host(host):
        return {"error": "Invalid host"}, 400
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Simple validation example, more comprehensive checks may be required
    return host.isalnum() and '.' in host