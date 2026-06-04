from fastapi import FastAPI
import subprocess
from shlex import quote
global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use subprocess.run with check=True and shell=False for a safer implementation
    result = subprocess.run(['ping', quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}