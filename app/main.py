from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        args = list(shlex.split(command)) + list(args)
        return subprocess.call(args, **kwargs)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    SafeSubprocess.call(f"ping", host)
    return {"status": "completed"}