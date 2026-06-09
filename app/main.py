from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent shell injection
    if not host.strip() or host.isnumeric():
        return {"error": "Invalid input"}, 400
    command = ["ping", *shlex.split(host)]
    subprocess.run(command)
    return {"status": "completed"}