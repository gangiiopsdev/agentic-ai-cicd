from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using check_output to avoid shell=True and capture output
    args = shlex.split(f"ping {host}")
    result = subprocess.check_output(args, stderr=subprocess.STDOUT)
    return {"status": "completed", "output": result.decode()}