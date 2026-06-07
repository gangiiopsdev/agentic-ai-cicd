from fastapi import FastAPI
import subprocess

global_params = {
    "ping": "/bin/ping",
}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run([global_params["ping"], host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}