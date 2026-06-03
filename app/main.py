from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    # Safe implementation using args instead of shell=True
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    _ping(host)
    return {"status": "completed"}