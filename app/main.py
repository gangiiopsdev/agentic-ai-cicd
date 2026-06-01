from fastapi import FastAPI
import subprocess
glances = subprocess.run(['ping', host], capture_output=True, text=True)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    glances = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": glances.stdout}