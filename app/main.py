from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_str if c in allowed_chars)

def safe_ping(host: str):
    # Validate the host format to avoid potential injection
    import re
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid host format')
    args = ['ping', sanitized_host]
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    safe_ping(sanitized_host)
    return {"status": "completed"}