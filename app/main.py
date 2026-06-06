from fastapi import FastAPI
import subprocess

app = FastAPI()

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    # Fixed implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

app.get('/', endpoint=home)
app.get('/ping', endpoint=ping)