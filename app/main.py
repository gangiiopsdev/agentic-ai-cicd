from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    try:
        return ''.join(shlex.split(input_string))
    except ValueError:
        raise ValueError('Invalid input')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        if not sanitized_host.isalnum():
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}