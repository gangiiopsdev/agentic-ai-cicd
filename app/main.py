from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with shell=False and executable=None to mitigate command injection
    subprocess.run(['ping', host], check=True, shell=False, executable=None)
    return {"status": "completed"}