from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str):
    args = ['ping', quote(host)]
    return subprocess.run(args, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        return {"error": "Invalid input"}, 400
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}