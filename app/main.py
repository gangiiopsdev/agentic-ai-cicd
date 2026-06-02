from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isdigit():
        return {"status": "invalid input"}
    result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {
        "status": "completed",
        "stdout": result.stdout.decode('utf-8'),
        "stderr": result.stderr.decode('utf-8')
    }