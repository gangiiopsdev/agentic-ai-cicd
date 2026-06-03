from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and use of check_output for safer execution
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host name"}, 400
    try:
        subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=10)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 500
    return {"status": "completed"}