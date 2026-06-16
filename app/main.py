from fastapi import FastAPI
import subprocess
from shlex import quote
def escape_input(input_str):
    return quote(input_str)

def safe_ping(host: str):
    command = ['ping', host]
    subprocess.run(command, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}