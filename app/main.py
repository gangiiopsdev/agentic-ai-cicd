from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or len(host) > 255:
        return False
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    if safe_ping(host):
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": "Invalid host name"}