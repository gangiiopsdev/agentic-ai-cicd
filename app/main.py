from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)