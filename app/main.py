from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    try:
        args = ['ping', '-c', '4', host]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()} 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    try:
        args = ['ping', '-c', '4', shlex.quote(host)]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", 'error': e.output.decode()}