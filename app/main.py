from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Safe implementation using subprocess.run with shell=False and properly formatted command
    result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}