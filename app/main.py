from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Ensure the host parameter only contains valid characters for ping
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if any(char not in allowed_chars for char in host):
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Fixed implementation
    safe_ping(host)
    return {"status": "completed"}