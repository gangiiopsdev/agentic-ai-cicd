from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a list for the command and avoiding shell=True
    if not host.isnumeric() or len(host) != 4:
        raise HTTPException(status_code=400, detail="Invalid host format")
    subprocess.call(['ping', host])
    return {"status": "completed"}