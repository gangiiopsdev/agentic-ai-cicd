from fastapi import FastAPI
import subprocess
global ping_count
ping_count = 0

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_count
    if ping_count < 10:
        subprocess.call(["ping", host])
        ping_count += 1
    else:
        return {"status": "Too many pings"}