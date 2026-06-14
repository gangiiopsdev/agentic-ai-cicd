from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use check_output with shell=False to avoid command injection
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed", "result": result.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}