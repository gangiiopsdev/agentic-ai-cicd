from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use the check_output method to avoid shell=True and execute command safely
        result = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return {"status": "completed", "result": result.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}