from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not all(c.isalnum() or c in ('-', '.') for c in host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):