from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or not host.isalnum():
        return 'Invalid host'
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)