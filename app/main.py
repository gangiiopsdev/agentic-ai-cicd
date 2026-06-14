from fastapi import FastAPI
import subprocess

def run_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {str(e)}'

def sanitize_input(input_string):
    import re
    if not re.match(r'^[a-zA-Z0-9-]+$', input_string):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitize_input(host)
    except ValueError as e:
        return str(e)
    return run_ping(host)