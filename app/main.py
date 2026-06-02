from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    sanitized = ''.join(filter(allowed_chars.__contains__, user_input))
    return sanitized

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c in allowed_chars for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(f"ping {host}", shell=False)
    return {'status': 'completed'}