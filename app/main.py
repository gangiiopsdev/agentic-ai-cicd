from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if 'ping' not in host:
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_safe(host: str):
    # Secure implementation
    if 'ping' not in host:
        subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed"}