from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host:
        raise ValueError('Host parameter is required')
    # Sanitize input to prevent command injection
    args = ['ping', subprocess.quote(host)]
    subprocess.run(args, check=True, shell=False)

    return {'status': 'completed'}