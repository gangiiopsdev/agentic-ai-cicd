from fastapi import FastAPI
import subprocess

def safe_ping(host):
    ping_command = ['ping', host]
    subprocess.run(ping_command, check=True, capture_output=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host.replace(';', '').replace('&', ''))
    return {'status': 'completed'}