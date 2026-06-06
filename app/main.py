from fastapi import FastAPI
import subprocess
import shlex

global host_whitelist = {'google.com', 'example.com'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    if host not in host_whitelist:
        raise ValueError("Host is not allowed")

    # Secure implementation
    subprocess.call(shlex.split(f"ping {host}"))

    return {"status": "completed"}