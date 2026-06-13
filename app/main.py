from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Use shlex.quote to safely quote the host argument
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class FastAPI:
    def __init__(self):
        pass

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}