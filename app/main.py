from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper arguments
    sp.run(['ping', host], check=True)
    return {"status": "completed"}