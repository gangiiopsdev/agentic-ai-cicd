from fastapi import FastAPI
import subprocess
global_dict = globals()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or len(host) > 15:
        raise ValueError("Invalid host name")
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}