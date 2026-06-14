from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation to prevent basic malicious inputs
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(c in allowed_chars for c in host)

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}