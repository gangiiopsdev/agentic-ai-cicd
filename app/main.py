from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain harmful characters
    if any(char in host for char in [';', '&', '|', '`', '$']):
        return {"error": "Invalid host input"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}