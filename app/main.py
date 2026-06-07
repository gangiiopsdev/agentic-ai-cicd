from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', sanitized_host], shell=False)

    return {"status": "completed"}