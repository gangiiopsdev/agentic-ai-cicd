from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"`
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input for ping host")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}