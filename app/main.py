from fastapi import FastAPI
import subprocess
glances = ['ping', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(glances, shell=False)
    return {'status': 'completed'}