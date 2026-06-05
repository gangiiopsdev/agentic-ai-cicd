from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.run(["ping", shell_quote(host)], check=True)
    return {"status": "completed"}