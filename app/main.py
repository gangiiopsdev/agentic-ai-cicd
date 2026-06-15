from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.call with args instead of shell=True and shlex.quote for safe command arguments
    subprocess.call(['ping', shlex.quote(host)])
    return {"status": "completed"}