from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and use of shlex for safe splitting of arguments
    if host.strip().isalnum() and len(host) <= 15:
        subprocess.run(['ping', *shlex.split(host)], check=True)
    return {"status": "completed"}