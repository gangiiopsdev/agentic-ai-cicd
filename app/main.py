from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host: str) -> bool:
    if not host.isalnum() or len(host) > 64:
        return False
    # Additional checks for malicious patterns can be added here
    return True

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}