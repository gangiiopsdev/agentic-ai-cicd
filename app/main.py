from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in input_str if c in allowed_chars)

def safe_subprocess(command, args=None):
    result = []
    for arg in args:
        if isinstance(arg, str) and "&" in arg or "$" in arg or ";" in arg:
            raise ValueError("Command injection detected")
        result.append(subprocess.call([command] + arg.split()))
    return result

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        args = ['ping', *map(safe_subprocess, [sanitized_host], shell=False)]
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}