from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ["-"] for c in host):
        return {"status": "error", "output": "Invalid host name"}
    try:
        output = subprocess.check_output(["ping", host], timeout=10, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}
    except subprocess.TimeoutExpired:
        return {"status": "timeout"}