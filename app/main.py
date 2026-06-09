from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using list for subprocess arguments
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation using list for subprocess arguments
    subprocess.call(['ping', host])
    return {"status": "completed"}