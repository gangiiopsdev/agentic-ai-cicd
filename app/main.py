from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_call(command_parts):
        return subprocess.run(command_parts, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_parts = shlex.split(f"ping {host}")
    result = SafeSubprocess.safe_call(command_parts)
    return {"status": "completed", "output": result.stdout}