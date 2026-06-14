from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using list for command arguments
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}