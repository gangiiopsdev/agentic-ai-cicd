from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(filter(allowed_chars.__contains__, input_string))
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', *shlex.split(sanitized_host)]  # Use shlex to safely split the sanitized host
    subprocess.run(command, check=True)
    return {'status': 'completed'}