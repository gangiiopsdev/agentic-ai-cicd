from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.Popen instead of subprocess.call for better control
    ping_command = ['ping', host]
    subprocess.run(ping_command, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}