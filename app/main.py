from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if host.startswith('192.168.1.') or host.startswith('10.0.0.'):  # Example IP validation
        subprocess.call(['ping', host])
    else:
        return {"status": "Invalid host"}

    return {"status": "completed"}