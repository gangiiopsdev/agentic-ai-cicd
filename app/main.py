from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using Popen and list of arguments
    subprocess.Popen(["ping", host], shell=False)
    return {"status": "completed"}