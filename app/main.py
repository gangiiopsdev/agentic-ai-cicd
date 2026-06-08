from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, **kwargs)

app = FastAPI()

@app.get("/""
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Safe implementation
    SafeSubprocess.safe_call(f"ping {host}")

    return {"status": "completed"}