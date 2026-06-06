from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use a safe implementation to avoid command injection
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}