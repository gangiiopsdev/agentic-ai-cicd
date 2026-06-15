from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.strip().startswith('-'):  # Prevents injection of options like -c
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1', host]  # Use '-c' to limit the number of pings
    subprocess.call(command)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}