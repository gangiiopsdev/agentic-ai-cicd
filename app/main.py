from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "result": result.stdout}