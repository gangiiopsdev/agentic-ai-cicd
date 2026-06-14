from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(hostname):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(char in allowed_chars for char in hostname)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host name")
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}