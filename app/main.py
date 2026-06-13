from fastapi import FastAPI
import subprocess
def escape_command(input):
    return input.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = escape_command(host)
    subprocess.call(f'ping {safe_host}')
    return {'status': 'completed'}