from fastapi import FastAPI
import subprocess
import shlex

cimport = subprocess.run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = cimport(f'ping {shlex.quote(host)}', capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except subprocess.TimeoutExpired:
        return {"status": "timeout"}