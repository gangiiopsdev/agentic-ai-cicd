from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid input")
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}