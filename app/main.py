from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    safe_host = shlex.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping(host)
    return {"status": "completed"}