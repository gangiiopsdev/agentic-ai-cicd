from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: ['ping', quote(host)]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(generate_ping_command(host))
    return {"status": "completed"}