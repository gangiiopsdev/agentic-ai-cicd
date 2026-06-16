from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    if not all(c.isalnum() or c in '-.' for c in input_string):
        raise ValueError('Invalid characters in input')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}