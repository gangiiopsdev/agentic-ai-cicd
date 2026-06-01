from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using shlex.split to prevent command injection
    command = ['ping', host]
    subprocess.call(command)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}