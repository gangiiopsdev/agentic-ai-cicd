from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command, *args, **kwargs):
        if isinstance(command, str):
            parts = command.split()
        else:
            parts = command
        return subprocess.call(parts, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    SafeSubprocess.call(["ping", host])
    return {"status": "completed"}