from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = ['ping', '-c', '1', host]
    subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}