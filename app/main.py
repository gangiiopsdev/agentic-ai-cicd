from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, host))
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.call(args)
    return {'status': 'completed'}