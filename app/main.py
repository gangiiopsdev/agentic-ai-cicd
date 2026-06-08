from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using f-string to safely escape shell arguments
    command = ['ping', host]
    subprocess.call(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}