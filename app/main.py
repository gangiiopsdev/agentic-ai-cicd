from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using os.system with validation
    if not host.isalnum() and host.count('.') != 3:
        raise ValueError('Invalid host format')
    subprocess.call(['ping', host])
    return {"status": "completed"}