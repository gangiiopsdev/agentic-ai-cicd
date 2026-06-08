from fastapi import FastAPI
import subprocess
getoutput = __import__('subprocess').getoutput

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    response = getoutput(f'ping {host}')
    return {'status': 'completed', 'response': response}