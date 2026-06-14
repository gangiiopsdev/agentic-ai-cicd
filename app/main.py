from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safer implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}