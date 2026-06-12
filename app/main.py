from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(filter(lambda x: x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-', input_string))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    cmd = ['ping', sanitized_host]
    subprocess.call(cmd, shell=False)
    return {'status': 'completed'}