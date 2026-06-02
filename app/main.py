from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use check_output to avoid shell=True and potential command injection
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    return {"status": "completed"}