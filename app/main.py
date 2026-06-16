from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in valid_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    # Secure implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}