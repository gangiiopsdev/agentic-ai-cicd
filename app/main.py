from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and argument unpacking
    args = shlex.split(host)
    subprocess.run(["ping"] + args, check=True)
    return {"status": "completed"}