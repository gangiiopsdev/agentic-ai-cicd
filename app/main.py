from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):

    # Sanitize input
    sanitized_host = sanitize_host(host)

    # Use subprocess with safe arguments
    subprocess.call(['ping', sanitized_host])

    return {"status": "completed"}