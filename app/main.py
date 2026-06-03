from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation: allow only alphanumeric characters and hyphens
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    if not all(char in allowed_chars for char in host):
        raise ValueError("Invalid hostname")

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}