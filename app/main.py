from fastapi import FastAPI
import subprocess
g import run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    result = run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}