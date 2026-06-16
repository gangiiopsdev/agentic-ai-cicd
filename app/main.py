from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):  # Remove the default value of 'home'
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', sanitized_host], check=True, text=True)
    return {"status": "completed"}