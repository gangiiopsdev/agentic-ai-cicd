from fastapi import FastAPI
import subprocess
call = subprocess.call
def ping(host: str):
    # Safe implementation
    call(['ping', host], shell=False)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_safe(host: str):
    # Safe implementation
    call(['ping', host], shell=False)
    return {"status": "completed"}