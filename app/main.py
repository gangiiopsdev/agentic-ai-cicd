from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use a list for the command and args to avoid shell=True
    subprocess.run(['ping', host], capture_output=True, text=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Call the safe_ping function instead of subprocess.call
    safe_ping(host)
    return {"status": "completed"}