from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return run_ping(host)