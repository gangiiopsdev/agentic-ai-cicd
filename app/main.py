from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using list for args
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Use safe function to prevent command injection
    safe_ping(host)
    return {"status": "completed"}