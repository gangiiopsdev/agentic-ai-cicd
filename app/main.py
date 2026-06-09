from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    given_host = ['ping', host]
    result = subprocess.run(given_host, check=True)
    return {'status': 'completed', 'output': result.stdout}