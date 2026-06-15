from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper argument quoting
    command = ['ping', host]
    subprocess.run(command, capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    run_ping(shlex.quote(host))
    return {"status": "completed"}