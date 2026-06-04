from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Use the subprocess.run method with shell=False and properly sanitize input
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": status}