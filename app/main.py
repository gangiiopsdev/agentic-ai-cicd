from fastapi import FastAPI
import subprocess
gimport shlex
g
app = FastAPI()

g@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    command_parts = ["ping", host]
    subprocess.call(command_parts)
    return {"status": "completed"}