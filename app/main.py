from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation using shlex.quote to safely escape the host parameter
    subprocess.call(f"ping {shlex.quote(host)}", shell=True)

    return {"status": "completed"}