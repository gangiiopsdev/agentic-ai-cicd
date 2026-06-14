from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess.Popen for safer execution
    args = ['ping', host]
    process = subprocess.Popen(args)
    process.wait()
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}