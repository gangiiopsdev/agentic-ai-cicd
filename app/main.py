from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        process = Popen(['ping', '-c', '1', host], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate(timeout=5)
        return {'status': 'completed' if not error else 'failed', 'output': output.decode('utf-8'), 'error': error.decode('utf-8')}
    except subprocess.TimeoutExpired:
        return {'status': 'failed', 'error': 'Process timed out'}