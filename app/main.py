from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return shlex.quote(input_string)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}