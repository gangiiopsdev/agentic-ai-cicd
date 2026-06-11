from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = sp.run(args, stdout=sp.PIPE, stderr=sp.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8'), 'error': result.stderr.decode('utf-8')}