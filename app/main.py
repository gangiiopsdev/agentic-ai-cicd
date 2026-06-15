from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host or ' ' in host:
        return {'status': 'Invalid input'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': e.stderr.decode()}
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}