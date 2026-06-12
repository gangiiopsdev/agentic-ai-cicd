from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return "Invalid input"
    subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": result}