from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(filter(allowed_chars.__contains__, input_str))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host.isalnum() or '.' in sanitized_host:
        args = ['ping', '--', sanitized_host]
        subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid input'}