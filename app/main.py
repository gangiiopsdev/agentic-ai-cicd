from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command_parts):
    try:
        output = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ['8.8.8.8', '127.0.0.1']:  # Example safe hosts, replace with actual validation logic
        command_parts = ['ping', shlex.quote(host)]
        return safe_subprocess(command_parts)
    else:
        return {"status": "failed", "error": "Host not allowed"}