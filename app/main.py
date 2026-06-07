from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using check_output with shell=False and passing the command as a list
    subprocess.check_call(["ping", host], shell=False)
    return {"status": "completed"}