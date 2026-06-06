from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host):
    ping_command = ['ping', '-c', '1', host]
    try:
        output = subprocess.run(ping_command, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}