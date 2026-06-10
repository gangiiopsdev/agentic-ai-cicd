from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess safely without shell=True
    subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use safe function
    safe_ping(host)
    return {"status": "completed"}