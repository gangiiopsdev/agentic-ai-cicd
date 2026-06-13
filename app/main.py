from fastapi import FastAPI
import subprocess
git from subprocess import Popen, PIPE

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation using Popen instead of shell=True
    process = Popen(['ping', host], stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()

    return {"status": "completed", "output": output.decode(), "error": error.decode()}