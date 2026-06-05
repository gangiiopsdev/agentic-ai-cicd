from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using shlex.quote to escape host input
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}