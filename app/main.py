from fastapi import FastAPI
import subprocess
gimport shlex
g
app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(c for c in host if c in allowed_chars)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping -c 1 {shlex.quote(sanitized_host)}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}