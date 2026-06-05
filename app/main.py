from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    result = subprocess.run(['ping', host], stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)