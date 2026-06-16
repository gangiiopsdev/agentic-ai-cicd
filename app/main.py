from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        process = Popen(['ping', host], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": error.decode()}