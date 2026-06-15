from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation using subprocess.Popen
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}