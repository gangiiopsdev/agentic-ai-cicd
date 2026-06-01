from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to escape the host argument
    from shlex import quote
    safe_host = quote(host)
    subprocess.call(f"ping {safe_host}", shell=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": "completed"}