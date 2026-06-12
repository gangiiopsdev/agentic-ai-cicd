from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        # Use shlex to safely split the command into arguments
        safe_command = shlex.split(command)
        return subprocess.run(safe_command, capture_output=True, text=True, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    SafeSubprocess.run('ping', host, capture_output=True, text=True)
    return {"status": "completed"}