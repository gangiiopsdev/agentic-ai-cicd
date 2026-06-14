from fastapi import FastAPI
import subprocess
def ping_safe(host: str):
    args = ['ping', host]
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_safe(host)
    return {"status": "completed"}