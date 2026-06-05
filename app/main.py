from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    safe_host = shlex.quote(host)
    return subprocess.run(["ping", safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}