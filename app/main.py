from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input to prevent command injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    sanitized_host = ''.join(c for c in host if c in allowed_chars)
    try:
        result = subprocess.run(['ping', '-c', '1', f'/bin/ping', sanitized_host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return f"Failed to ping: {e.stderr}"
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}