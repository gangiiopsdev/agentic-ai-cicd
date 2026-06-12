from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        parts = shlex.split(command)
        return subprocess.run(parts, capture_output=True, text=True, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = SafeSubprocess.run(f'ping {host}')
    return {"status": "completed", "output": result.stdout}