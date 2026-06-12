from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():  # Simple validation, improve as needed
        return {'error': 'Invalid input'}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}