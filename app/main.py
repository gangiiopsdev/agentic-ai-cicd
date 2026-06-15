from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ''.join(filter(str.isalnum, host))[:20]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host != host:
        return {"status": "error", "message": "Invalid input"}
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}