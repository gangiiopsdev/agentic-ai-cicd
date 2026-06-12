from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}