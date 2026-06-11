from fastapi import FastAPI
import subprocess
gt from shlex import quote

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(f'ping {quote(host)}', shell=True)

    return {"status": "completed"}