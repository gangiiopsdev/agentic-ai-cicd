from fastapi import FastAPI
import subprocess
cimport os
def ping(host: str):
    # Safe implementation using subprocess.run
    if host:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'output': result.stdout}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run
    if host:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'output': result.stdout}