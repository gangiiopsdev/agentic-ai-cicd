from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in [',', '.', '_', '-'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}