from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using subprocess.run with a list to avoid shell injection
    subprocess.run(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}