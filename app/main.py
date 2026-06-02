from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Sanitize input using shlex.quote to prevent command injection
    safe_host = shlex.quote(host)

    subprocess.call(f'ping {safe_host}', shell=True)

    return {"status": "completed"}