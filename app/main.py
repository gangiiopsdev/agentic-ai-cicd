from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def run_ping(host):
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = run_ping(host)
    return {"status": "completed", "output": output}