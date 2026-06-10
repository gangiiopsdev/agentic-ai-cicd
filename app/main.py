from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using list instead of string for shell=True
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}