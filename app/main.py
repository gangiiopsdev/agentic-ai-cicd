from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using check_output to avoid shell=True
    try:
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "result": result.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}