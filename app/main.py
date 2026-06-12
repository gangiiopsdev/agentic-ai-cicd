from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = shlex.quote(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'output': result.stdout}