from fastapi import FastAPI
import subprocess
from os.path import abspath, join

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    full_path = abspath(join('/usr/bin', 'ping'))
    subprocess.run([full_path, host], check=True)
    return {"status": "completed"}