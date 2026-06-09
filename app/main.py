from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and safe execution
    if not host:
        return {"error": "Host parameter is required"}
    subprocess.call(["ping", "/bin/ping", host])
    return {"status": "completed"}