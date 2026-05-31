from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
globally_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        process = Popen(['ping', '-c', '1', host], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}
    else:
        return {"status": "error", "message": "Unauthorized host"}