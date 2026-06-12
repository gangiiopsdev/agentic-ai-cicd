from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation: only allow alphanumeric characters and a few special characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    if not all(char in allowed_chars for char in host):
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}