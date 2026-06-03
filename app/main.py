from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"付费)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and f-string formatting to avoid command injection.
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}