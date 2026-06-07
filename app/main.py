from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in input_string)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host], shell=False)
    return {'status': 'completed'}