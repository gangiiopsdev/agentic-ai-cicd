from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    sanitized = ''.join(filter(allowed_chars.__contains__, input_str))
    return sanitized

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'invalid_host'}
    subprocess.run(['ping', shlex.quote(sanitized_host)], check=True, text=True)
    return {'status': 'completed'}