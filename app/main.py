from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():
        return {'error': 'Invalid input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}

@app.get="/"
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get="/ping"
def ping(host: str):
    return safe_ping(host)