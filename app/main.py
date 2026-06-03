from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Basic sanitization example: allow only alphanumeric characters and hyphens
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Safe implementation with basic sanitization
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", 'message': e.stderr}