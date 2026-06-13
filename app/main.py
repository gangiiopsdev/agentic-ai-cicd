from fastapi import FastAPI
import subprocess
cimport = ('ping', 'example.com')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in cimport:
        return {'error': 'Invalid host'}
    subprocess.run(('ping', host), check=True, shell=False)
    return {'status': 'completed'}