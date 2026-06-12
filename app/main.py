from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_ping(host):
    args = ['ping', host]
    subprocess.call(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    run_safe_ping(host)
    return {"status": "completed"}