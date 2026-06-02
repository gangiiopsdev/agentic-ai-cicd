from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.')
    return ''.join(c for c in input_string if c in allowed_characters)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}