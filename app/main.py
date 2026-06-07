from fastapi import FastAPI
import subprocess
global_args = ['ping', 'google.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(global_args)

    return {'status': 'completed'}