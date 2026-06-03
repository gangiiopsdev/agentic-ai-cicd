from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    if isinstance(input_string, str) and input_string.strip().lower() in ['localhost', '127.0.0.1']:
        return input_string
    else:
        raise ValueError('Invalid host input')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        args = ['ping', shlex.quote(sanitized_host)]  # Use shlex.quote to sanitize the input
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}