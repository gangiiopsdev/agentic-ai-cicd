from fastapi import FastAPI
import subprocess
call = subprocess.call

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    call(["ping", host], shell=False)

    return {"status": "completed"}