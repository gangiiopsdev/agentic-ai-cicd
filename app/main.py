from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.Popen without shell=True
    subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}