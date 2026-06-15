from fastapi import FastAPI
import subprocess
cimport = ['127.0.0.1']  # Define a safe list of allowed hosts

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if host not in allowed_hosts:
        raise HTTPException(status_code=400, detail="Invalid host")
    subprocess.call(["ping", host])
    return {"status": "completed"}