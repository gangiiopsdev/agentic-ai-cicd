from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with shlex to safely handle the command argument
    subprocess.call(['ping', shlex.quote(host)])
    return {"status": "completed"}