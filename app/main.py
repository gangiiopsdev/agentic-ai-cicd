from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE

def ping(host: str):
    try:
        process = Popen(['ping', host], stdout=PIPE, stderr=PIPE, timeout=10)
        output, error = process.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        process = Popen(['ping', host], stdout=PIPE, stderr=PIPE, timeout=10)
        output, error = process.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': str(e)}