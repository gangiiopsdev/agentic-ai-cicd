from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell check and full executable path
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}