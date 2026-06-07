from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with additional checks
    if not host.isdigit():  # Basic input validation
        return {'status': 'invalid input'}, 400
    args = ['ping', *shlex.split(host)]
    subprocess.call(args)
    return {'status': 'completed'}