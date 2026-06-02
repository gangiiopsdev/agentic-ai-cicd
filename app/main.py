from fastapi import FastAPI
import subprocess

app = FastAPI()

glom = lambda x: subprocess.run(x, check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    glom(['ping', host])
    return {'status': 'completed'}