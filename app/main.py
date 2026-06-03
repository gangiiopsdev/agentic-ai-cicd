from fastapi import FastAPI
import subprocess
from typing import List
def safe_subprocess(command: List[str]):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Error executing command: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_subprocess(['ping', host])
    return {"status": "completed"}