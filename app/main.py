from fastapi import FastAPI
import subprocess
from shlex import quote
def run_ping(host):
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():  # Simple validation to check if the input is numeric (example)
        return {"error": "Invalid host input"}
    output = run_ping(host)
    return {"status": "completed", "output": output}