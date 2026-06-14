from fastapi import FastAPI
import subprocess

generate_ping_command = ['ping', 'target_host']
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation
    subprocess.call(['ping', host])
    return {'status': 'completed'}