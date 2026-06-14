from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command_parts):
    return subprocess.check_output(command_parts, stderr=subprocess.STDOUT, timeout=5)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command_parts = shlex.split(f'ping -c 4 {host}')
        output = safe_subprocess(command_parts)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.output.decode()}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "Ping request timed out"}