from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.Popen to avoid shell=True
    if not host.strip():
        raise ValueError("Invalid host")
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}