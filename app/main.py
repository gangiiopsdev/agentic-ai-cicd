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
    subprocess.run(command_parts, check=True)
    return {"status": "completed"}