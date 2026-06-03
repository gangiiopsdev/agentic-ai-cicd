from fastapi import FastAPI
import subprocess
from shlex import quote

global ping_func
ping_func = None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.on_event('startup')
def on_startup():
    global ping_func
    ping_func = subprocess.run,

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper sanitization
    if not ping_func:
        raise Exception('Ping function not initialized')
    sanitized_host = quote(host)
    result = ping_func(f'ping {sanitized_host}', check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}