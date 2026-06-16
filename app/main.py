from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    if not host.strip().isalnum() or len(host) > 255:
        return {"status": "failed", "error": "Invalid host input"}
    try:
        command = ['ping', '-c', '1', host]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=10)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}