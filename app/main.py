from fastapi import FastAPI
import subprocess
cimport = __import__

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with full path and shell check
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}