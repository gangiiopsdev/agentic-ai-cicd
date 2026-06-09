from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(filter(str.isalnum, user_input))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}