from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Replace host with escaped value or use subprocess.run safely
    subprocess.call(["ping", host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}