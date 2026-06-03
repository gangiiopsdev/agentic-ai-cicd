from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(value):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in value if char in allowed_chars)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation using subprocess.run with shlex.split for safer splitting of arguments
    subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, text=True)
    return {'status': 'completed'}