from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with shlex.split and shell=False
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):  # Basic validation to prevent shell injection
        return {"status": "Invalid input"}
    safe_ping(shlex.quote(host))
    return {"status": "completed"}

def validate_host(host:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(c in allowed_chars for c in host):
        return True
    return False