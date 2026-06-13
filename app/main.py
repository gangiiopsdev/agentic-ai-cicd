from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run to safely handle user input and capture output
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}