from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if any(char in input_string for char in [';', '&', '|', '*', '?', '<', '>', '$']):
        raise ValueError('Invalid characters in input')

@app.get="/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        subprocess.call(['ping', sanitized_host])
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400