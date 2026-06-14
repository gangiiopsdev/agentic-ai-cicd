from fastapi import FastAPI
import subprocess
git from shlex import quote

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f'ping {quote(host)}')
    return {"status": "completed"}