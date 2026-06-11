from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize the input to prevent command injection
    sanitized_host = ''.join(char for char in host if char.isalnum() or char in '.-')
    return subprocess.call(['ping', sanitized_host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}