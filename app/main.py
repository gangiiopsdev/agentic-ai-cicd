from fastapi import FastAPI
import subprocess
import shlex

callable_ping = lambda host: subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = subprocess.run(callable_ping(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}