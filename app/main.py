from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Use shlex to safely split the command into arguments
        args = shlex.split(f'ping {host}')
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex to safely split the command into arguments
        args = shlex.split(f'ping {host}')
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'