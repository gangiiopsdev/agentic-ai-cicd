from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.Popen with arguments
    subprocess.run(['ping', sanitized_host], check=True, text=True, capture_output=True)
    return {"status": "completed"}