from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.startswith('192.168.') or host.startswith('172.'):  # Example of input validation
        subprocess.call(['ping', host])
    else:
        return {"error": "Invalid host address"}

    return {"status": "completed"}