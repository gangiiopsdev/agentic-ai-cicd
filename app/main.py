from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call to avoid shell=True and for better security
    ping_command = ['ping', host]
    result = subprocess.run(ping_command, capture_output=True, text=True)
    return result.stdout,

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}