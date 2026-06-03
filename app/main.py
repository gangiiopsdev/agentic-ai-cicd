from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)  # Changed to use shell=True for demonstration purposes, but this should be avoided if possible.
    return {"status": "completed"}