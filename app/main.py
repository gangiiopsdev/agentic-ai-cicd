from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def get_full_path(executable):
    full_path = shutil.which(executable)
    if not full_path:
        raise FileNotFoundError(f'Executable {executable} not found')
    return full_path

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.run([get_full_path('ping'), host], check=True)
    return {'status': 'completed'}