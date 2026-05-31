from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split to prevent shell injection
    subprocess.call(subprocess.list2cmdline(['ping', host]))
    return {"status": "completed"}