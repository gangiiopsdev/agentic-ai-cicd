from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation using shlex.quote to neutralize special elements
    from shlex import quote
    subprocess.call(f"ping {quote(host)}", shell=True)

    return {"status": "completed"}