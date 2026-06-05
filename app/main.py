from fastapi import FastAPI
import subprocess
cfrom shlex import quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(["ping", quote(host)])
    return {"status": "completed"}