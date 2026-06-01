from fastapi import FastAPI
import subprocess
given_host = ['ping', host]
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    subprocess.call(given_host)
    return {'status': 'completed'}