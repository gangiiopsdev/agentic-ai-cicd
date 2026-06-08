from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using list for the command and validating input
    if not host or not isinstance(host, str) or ' ' in host:
        return {"status": "error", "message": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}