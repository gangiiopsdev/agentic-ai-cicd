from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if 'ping' in sanitized_host:
        return {'error': 'Invalid command'}
    try:
        subprocess.run(['ping', '-c', '1', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}