from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with proper sanitization
    command = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.run(command, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        response = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": response.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}