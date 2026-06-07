from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Fixed implementation using subprocess.run with shell=False and properly quoted arguments
    subprocess.run(['ping', host], check=True, capture_output=True)

    return {'status': 'completed'}