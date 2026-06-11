from fastapi import FastAPI
import subprocess
from shlex import quote

def safe_ping(host: str):
    try:
        result = subprocess.run(["ping", "-c", "1", quote(host)], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)