from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 64:
        raise ValueError('Invalid hostname')

    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

    return {'status': 'completed'}