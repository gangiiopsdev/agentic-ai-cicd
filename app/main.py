from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c.isdigit() or c == '-.')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the host input to prevent command injection
        sanitized_host = sanitize_input(host)
        if not sanitized_host.isalnum() or '-' not in sanitized_host or '.' not in sanitized_host:
            raise ValueError('Invalid host name')
        subprocess.run(['ping', quote(sanitized_host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except ValueError as ve:
        return {'error': str(ve)}