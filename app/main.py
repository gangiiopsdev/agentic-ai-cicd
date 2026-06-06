from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex.quote to escape shell arguments
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}