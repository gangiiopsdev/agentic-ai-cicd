from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

def sanitize_host(host: str) -> str:
    # Sanitize input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError('Invalid hostname')
    response = safe_ping(sanitized_host)
    return {"status": "completed", "response": response}