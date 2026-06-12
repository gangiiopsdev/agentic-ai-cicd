from fastapi import FastAPI
import subprocess

app = FastAPI()

global_args = ['ping', 'example.com']

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run(['ping'] + host.split(), check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}