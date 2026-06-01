from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():
        return {"status": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}