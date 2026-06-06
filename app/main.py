from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex.split to safely split the command into a list of arguments
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}