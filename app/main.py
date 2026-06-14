from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input
    if not host.strip() or ' ' in host:
        raise ValueError('Invalid host input')
    command = ['ping', '-c', '1'] + [shlex.quote(arg) for arg in shlex.split(host)]
    subprocess.run(command, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_safe(host: str):
    try:
        command = ['ping', '-c', '1'] + [shlex.quote(arg) for arg in shlex.split(host)]
        response = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": response.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}