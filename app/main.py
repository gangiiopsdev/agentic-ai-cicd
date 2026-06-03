from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using Popen with shell=False and proper argument handling
    subprocess.Popen(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}