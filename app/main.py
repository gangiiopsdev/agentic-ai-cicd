from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(allowed_chars.__contains__, host))

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}