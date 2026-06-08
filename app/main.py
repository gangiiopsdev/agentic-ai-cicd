from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation using shlex.quote to safely escape user input
    safe_host = shlex.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
    return {"status": "completed"}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}