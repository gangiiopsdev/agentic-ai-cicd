from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization
    if not host.isalnum():
        return {"error": "Invalid host name"}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e.output)}
    return {"status": "completed", "output": output}