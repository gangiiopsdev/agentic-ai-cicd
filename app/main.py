from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to safely handle user input
    safe_host = shlex.quote(host)
    subprocess.call(f"ping {safe_host}", shell=True)
    return {"status": "completed"}