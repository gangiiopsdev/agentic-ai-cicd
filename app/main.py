from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Safe implementation using list for args to prevent shell injection
    args = ['ping', host]
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}