from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and explicit arguments
    if not host:
        return {'status': 'error', 'message': 'Host parameter is required'}
    command = ["ping", host]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}