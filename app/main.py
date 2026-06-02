from fastapi import FastAPI
import subprocess
c import ping3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response_time = ping3.ping(host)
    if response_time is None:
        status = "failed"
    else:
        status = "completed"
    return {"status": status}