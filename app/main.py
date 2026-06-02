from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host == 'localhost' or host.startswith('192.168.'):
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    return ping(host)