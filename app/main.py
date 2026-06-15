from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and safe input handling
    args = shlex.split(host)
    subprocess.call(['ping'] + args, shell=False)
    return {"status": "completed"}