from fastapi import FastAPI
import subprocess
global_host = "example.com"  # Replace with actual host

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(["ping", host])  # Fixed code
    return {"status": "completed"}