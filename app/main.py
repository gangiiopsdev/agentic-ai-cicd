from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shlex to handle arguments safely
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}