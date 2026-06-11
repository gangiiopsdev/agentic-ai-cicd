from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], timeout=5, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    return {"status": "completed", "output": output.decode()}