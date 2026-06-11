from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_host = ''.join(filter(str.isdigit, host))  # Sanitize input to only allow digits for simplicity
    subprocess.call(['ping', safe_host], shell=False)
    return {"status": "completed"}