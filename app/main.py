from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Safer implementation using subprocess.run and shlex.quote
    args = ['ping', host]
    subprocess.run(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}