from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using subprocess.run with shlex.quote for argument quoting
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}