from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = ''.join(char for char in host if char.isalnum() or char in ('.', '-', '_'))
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}