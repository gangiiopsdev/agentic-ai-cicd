from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

def validate_and_sanitize_input(host):
    sanitized_host = sanitize_input(host)
    if any(char in ['&', '|', ';', '$', '`'] for char in sanitized_host):
        raise ValueError("Invalid input")
    return sanitized_host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validated_host = validate_and_sanitize_input(host)
        subprocess.Popen(['ping', '-c 1', validated_host], shell=False)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400