from fastapi import FastAPI
import subprocess
import shlex

global_result = {"status": "error", "output": "Unauthorized access attempt detected."}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host != 'localhost':
        return global_result
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}