from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host and all(c.isalnum() or c in "._-" for c in host):
        command = ["ping", shlex.quote(host)]
        subprocess.call(command)
    else:
        return {"error": "Invalid hostname"}
    return {"status": "completed"}