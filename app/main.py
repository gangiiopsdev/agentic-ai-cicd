from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum() or '..' in input_str:
        raise ValueError('Invalid host input')
    return input_str.replace('.', '')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}