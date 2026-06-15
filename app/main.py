from fastapi import FastAPI
import subprocess
from shlex import quote
def escape_input(input_str):
    return quote(input_str)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_input(host)
    subprocess.call(['ping', escaped_host])
    return {'status': 'completed'}