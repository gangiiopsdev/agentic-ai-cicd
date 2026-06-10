from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Simple validation example: allow only alphanumeric and a few special characters
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    sanitized_input = ''.join(char for char in input_str if char in allowed_chars)
    return sanitized_input

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}