from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed", "response": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "response": e.output.decode()}