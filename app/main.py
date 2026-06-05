from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(['ping', host], shell=False, check=True)
    return {'status': 'completed'}