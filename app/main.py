from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shell=False and argument list
    subprocess.call(['ping', '-c', '1', host], shell=False)
    return {"status": "completed"}