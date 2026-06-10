from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. '-
    return ''.join(filter(lambda x: x in allowed_chars, input_string))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}