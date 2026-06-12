from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and shlex.split for safe command construction
    command = ["ping", *shlex.split(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}