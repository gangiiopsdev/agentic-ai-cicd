from fastapi import FastAPI
import subprocess
def safe_ping(host):
    safe_host = host.replace(';', ' ').replace('&', '')
    subprocess.call(['ping', '-c', '1', safe_host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Secure implementation
    safe_ping(host)
    return {"status": "completed"}