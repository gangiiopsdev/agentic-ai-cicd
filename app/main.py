from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Simple sanitization, improve based on specific requirements
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "ping request timed out"}