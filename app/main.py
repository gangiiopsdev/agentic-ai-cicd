from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isdigit() and len(host.split('.')) == 4:
        args = ['ping', host]
        subprocess.run(args)
    else:
        return {"error": "Invalid host"}
    return {"status": "completed"}