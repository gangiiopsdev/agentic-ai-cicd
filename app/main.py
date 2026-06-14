from fastapi import FastAPI
import subprocess
cimport = set(['ping'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in cimport:
        raise ValueError('Invalid command')
    subprocess.call(['ping', host])  # Use subprocess.run with shell=False and list of arguments
    return {'status': 'completed'}