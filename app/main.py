from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError('Invalid hostname')

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

def validate_host(func):
    def wrapper(*args, **kwargs):
        host = kwargs.get('host')
        if host and not isinstance(host, str):
            raise ValueError('Host must be a string')
        return func(*args, **kwargs)
    return wrapper

@app.get('/ping')
def ping(host: str):  # Validate input using the decorator
    validate_host(ping)(host=host)
    return secure_ping(host)