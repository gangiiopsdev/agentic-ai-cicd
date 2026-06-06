from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    return subprocess.run(command, capture_output=True, text=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    result = run_command(command)
    return {'status': result.stdout, 'stderr': result.stderr}