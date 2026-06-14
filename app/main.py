from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not is_safe_hostname(host):
        raise ValueError('Unsafe hostname provided')
    args = shlex.split(f'ping {host}')
    subprocess.run(args)
    return {'status': 'completed'}

def is_safe_hostname(hostname: str) -> bool:
    # Basic validation, improve as needed
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.'
    for char in hostname:
        if char not in allowed_chars:
            return False
    return True