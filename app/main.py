from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command_parts):
    safe_command = shlex.join(command_parts)
    return subprocess.run(safe_command, shell=True, check=True, timeout=5)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_subprocess(['ping', host])
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}