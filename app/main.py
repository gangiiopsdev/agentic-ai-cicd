from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and splitting the command into a list
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}
    return {'status': 'completed', 'output': result.stdout}