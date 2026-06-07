from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_input(host)
    try:
        output = subprocess.check_output(['ping', escaped_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}