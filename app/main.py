from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using a whitelist of allowed hosts
    if host not in ['localhost', '127.0.0.1']:
        return {'status': 'failed', 'error': 'Host is not allowed'}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(shlex.split('ping ' + host), stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}