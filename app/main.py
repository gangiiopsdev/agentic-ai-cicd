from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen and shell=False to avoid execution of untrusted input
    process = subprocess.Popen(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return {"status": "error", "message": str(error)}
    else:
        return {"status": "completed", "output": str(output)}