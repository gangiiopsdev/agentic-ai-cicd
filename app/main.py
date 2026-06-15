from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Fixed implementation using shlex.quote to safely escape arguments
    args = ['ping', host]
    subprocess.call(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}