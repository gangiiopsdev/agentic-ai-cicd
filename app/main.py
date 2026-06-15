from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using check_output to avoid shell=True
    subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    return {"status": "completed"}