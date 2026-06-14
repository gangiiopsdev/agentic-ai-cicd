from fastapi import FastAPI
import subprocess
import shlex

global host
host = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.on_event("startup")
def startup_event():
    global host
    host = "example.com"

@app.get("/ping")
def ping():
    command_parts = shlex.split(f"ping {host}")
    try:
        subprocess.run(command_parts, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}