from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
globally_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts
def _run_ping(host):
    if host not in globally_safe_hosts:
        return {'status': 'error', 'message': 'Unauthorized host'}
    process = Popen(['ping', '-c', '1', host], stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return _run_ping(host)