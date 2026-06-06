from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    execute_ping(host)
    return {"status": "completed"}