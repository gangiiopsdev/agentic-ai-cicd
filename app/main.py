from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_input(input_string):
    # Basic regex check for potential malicious characters
    if re.search(r'[;`&|\]', input_string):
        raise ValueError('Invalid input')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_input(host)
    command = ['ping', *shlex.split(host)]
    subprocess.call(command)
    return {'status': 'completed'}