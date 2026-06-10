from fastapi import FastAPI
import subprocess
given_host = '8.8.8.8'  # Replace this with a safe default or input validation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host != given_host:
        return {"status": "Invalid host"}
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}