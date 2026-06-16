from fastapi import FastAPI
import subprocess
global_ping = ['ping', '127.0.0.1'] # Replace this with valid IP address or host.

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Fixed implementation
    subprocess.call(global_ping)

    return {'status': 'completed'}