from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', cmd_quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)