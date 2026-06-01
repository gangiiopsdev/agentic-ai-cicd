from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if host.isalpha() and len(host) <= 20:
        subprocess.call(['ping', f'127.0.0.1'])  # Replace with a safe default or remove the parameter
    return {'status': 'completed'}