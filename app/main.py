from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return host and len(host) <= 256

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid input"}
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}