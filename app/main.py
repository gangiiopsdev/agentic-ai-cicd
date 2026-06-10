from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(char for char in input_string if char.isalnum() or char in ('.', '-', '_'))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}