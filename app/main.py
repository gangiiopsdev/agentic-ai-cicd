from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(c for c in input_str if c in allowed_chars)

def safe_subprocess(command, args=None):
    result = []
    for arg in args:
        if isinstance(arg, str) and any(char in arg for char in ['&', '$', ';']):
            raise ValueError("Command injection detected")
        result.append(subprocess.call([command] + [arg]))
    return result

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        args = ['ping', sanitized_host]
        subprocess.run(args, check=True, shell=False)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}