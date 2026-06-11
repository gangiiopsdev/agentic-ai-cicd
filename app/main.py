from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in input_string):
        raise ValueError('Invalid characters in host name')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):