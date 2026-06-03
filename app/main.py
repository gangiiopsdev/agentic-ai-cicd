from fastapi import FastAPI
import subprocess
def execute_ping(host):
    if not host.isnumeric():
        raise ValueError("Invalid host")
    return subprocess.call(f'ping {host}', shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = execute_ping(host)
    return {'status': 'completed', 'result': result}