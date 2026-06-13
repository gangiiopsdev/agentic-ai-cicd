from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or ' ' in host:
        return {"status": "Invalid input"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}