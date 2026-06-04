from fastapi import FastAPI
import subprocess
glances = ['ping', '-c', '1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    subprocess.run(glances + [host])
    return {'status': 'completed'}