from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using Popen instead of call with shell=True
    subprocess.Popen(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}