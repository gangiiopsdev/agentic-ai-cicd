from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize user input
    safe_host = host.replace(';', '').replace('&', '').replace('|', '')
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping(host)