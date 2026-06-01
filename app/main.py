from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to escape the host input
    if not os.path.exists("/sbin/ping"):
        raise Exception("Ping executable not found")
    subprocess.run(["/sbin/ping", shlex.quote(host)], check=True)
    return {"status": "completed"}