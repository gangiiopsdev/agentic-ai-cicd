from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.Popen
    subprocess.Popen(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.Popen
    subprocess.Popen(['ping', host])