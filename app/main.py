from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use a whitelisted list of hosts or validate the input
    if host in ['example.com', 'localhost']:
        subprocess.call(['ping', host])
    return {'status': 'completed'}