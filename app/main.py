from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Basic sanitization of host input
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    result = subprocess.run(['ping', '-c', '1', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}