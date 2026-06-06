from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', sanitized_host], check=True, shell=False)  # Use subprocess.run with shell=False and check=True
    return {"status": "completed"}