from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def call(command_parts):
        subprocess.call(command_parts)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_parts = shlex.split(f"ping {host}")
    SafeSubprocess.call(command_parts)

    return {"status": "completed"}