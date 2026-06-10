from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    # Safe implementation using subprocess.run with shlex.split
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        execute_ping(shlex.quote(host))  # Use shlex.quote to sanitize input
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}