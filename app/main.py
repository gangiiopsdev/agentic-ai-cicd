from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        subprocess.call(['ping', sanitized_host], check=True)
        return {"status": "completed", "details": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "details": str(e)}