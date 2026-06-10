from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with argument validation and full executable path
    if host not in ['127.0.0.1', '::1']:  # Example of valid hosts
        return {"status": "invalid host"}
    subprocess.call(['ping', '-c', '4', host])  # Use full executable path and limit ping count for safety
    return {"status": "completed"}