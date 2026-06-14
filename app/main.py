from fastapi import FastAPI
import subprocess
cimport os
cimport sys

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail="Invalid host")
    command = ["ping", host]
    subprocess.call(command)
    return {"status": "completed"}

# Define a list of allowed hosts
allowed_hosts = ["example.com", "localhost"]