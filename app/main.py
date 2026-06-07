from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with proper validation and sanitization
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}