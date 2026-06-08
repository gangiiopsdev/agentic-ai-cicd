from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command, **kwargs):
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.run(command, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with proper sanitization and path check
    safe_hosts = ['8.8.8.8', '127.0.0.1']  # Example safe hosts
    if host not in safe_hosts:
        return {"status": "error", "message": "Invalid host"}
    result = SafeSubprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}