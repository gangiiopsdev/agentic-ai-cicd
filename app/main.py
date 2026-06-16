from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Safe implementation without using shell=True
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    run_ping(host)
    return {'status': 'completed'}