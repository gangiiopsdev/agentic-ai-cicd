from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        ip_address = subprocess.check_output(['nslookup', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e.output}'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)