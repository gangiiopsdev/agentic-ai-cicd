from fastapi import FastAPI
import subprocess
cimport = {'ping': 'ping'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in cimport:
        command = [cimport[host]]
        subprocess.run(command, check=True)
    else:
        return {'error': 'Invalid command'}
    return {'status': 'completed'}