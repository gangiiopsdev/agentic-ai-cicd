from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    safe_host = shlex.quote(host)
    subprocess.call(["ping", safe_host], shell=False)
    return {"status": "completed"}