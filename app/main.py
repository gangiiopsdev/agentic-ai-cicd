from fastapi import FastAPI
import subprocess

def execute_ping(host):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout, result.stderr

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    stdout, stderr = execute_ping(host)
    return {'status': 'completed', 'stdout': stdout, 'stderr': stderr}