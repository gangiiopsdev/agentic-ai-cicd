from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' 
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Safer implementation using subprocess.run
    sanitized_host = sanitize_host(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}