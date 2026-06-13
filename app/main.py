from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    p = sp.Popen(['ping', host], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = p.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}