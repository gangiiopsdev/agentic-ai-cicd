from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation without using shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):  # Add validation for the host parameter
        ping_safe(host)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Simple validation, adjust as needed
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in valid_chars for char in host)