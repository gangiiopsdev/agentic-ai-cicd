from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and input validation
    if host and host.strip() and re.match(r'^[a-zA-Z0-9.-]+$', host):
        subprocess.run(["ping", host], check=True)
    return {"status": "completed"}