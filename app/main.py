from fastapi import FastAPI
import subprocess
def sanitize_input(input_value):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in input_value if char in allowed_chars)

app = FastAPI()
ALLOWED_HOSTS = ['example.com', 'test.com']

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host in ALLOWED_HOSTS:
        subprocess.run(['ping', '-c', '1', f'"{sanitized_host}"'], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Host not allowed'}, 403