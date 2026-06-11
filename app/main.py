from fastapi import FastAPI
import subprocess
import shlex

global_ping = lambda host: subprocess.call(['ping', '-c', '1'] + shlex.split(host))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    global_ping(shlex.quote(host))
    return {"status": "completed"}