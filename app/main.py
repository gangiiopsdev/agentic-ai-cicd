from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(c in allowed_chars for c in host)

@app.get("/ping")
def ping(host: str):
    if not host:
        return {"status": "error", "message": "No host provided"}
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}