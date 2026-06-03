from fastapi import FastAPI
import subprocess
def escape_host(host: str):
    return host.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.run(['ping', '-c', '1', escaped_host], check=True, text=True)
    return {'status': 'completed'}