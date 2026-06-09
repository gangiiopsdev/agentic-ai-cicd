from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with check=True for proper error handling
    args = shlex.split(f"ping {host}")
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}