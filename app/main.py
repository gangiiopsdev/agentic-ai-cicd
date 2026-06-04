from fastapi import FastAPI
import subprocess
global_config = app.state.global_config

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}