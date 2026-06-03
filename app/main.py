from fastapi import FastAPI
import subprocess
import os

cwd = os.getcwd()
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True, capture_output=True, text=True, cwd=cwd)
    return {'status': 'completed'}