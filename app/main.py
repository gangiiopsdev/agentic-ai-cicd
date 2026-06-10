from fastapi import FastAPI
import subprocess
getattr(subprocess, 'call', getattr(subprocess, '_check_call'))(f'ping {host}', shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Secure implementation
    subprocess.run(f'ping {host}', shell=False)

    return {'status': 'completed'}