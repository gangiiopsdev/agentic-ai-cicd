from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    safe_ping(shlex.quote(host))
    return {"status": "completed"}