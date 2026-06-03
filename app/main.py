from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(filter(allowed_chars.__contains__, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}
    else:
        return {'status': 'completed'}