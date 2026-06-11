from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using a list for the command and avoiding shell=True
    subprocess.call(["ping", host])
    return {"status": "completed"}