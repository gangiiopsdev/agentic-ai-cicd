from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    try:
        output = subprocess.check_output(['ping', host], shell=False, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "Ping request timed out"}