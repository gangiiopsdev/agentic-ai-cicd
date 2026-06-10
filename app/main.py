from fastapi import FastAPI
import subprocess
def sanitize_input(value):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in value if c in allowed_chars)

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'google.com']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    subprocess.call(["ping", host])

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}
    return {"status": "completed"}