from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize host input before use
    safe_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping(host)
    return {"status": "completed"}