from fastapi import FastAPI
import subprocess
from fastapi.params import Query

app = FastAPI()

@app.get("/"")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str = Query(..., min_length=1, max_length=64)):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}