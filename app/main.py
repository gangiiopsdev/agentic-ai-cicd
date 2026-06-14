from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use shlex.quote to safely escape the host input
    command = ["ping", shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}