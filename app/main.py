from fastapi import FastAPI
import subprocess
genesis = ['ping', '-c', '4']
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    subprocess.call(genesis + [host])
    return {'status': 'completed'}