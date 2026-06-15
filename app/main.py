from fastapi import FastAPI
import subprocess
cimport os

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '-. ')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not all(c.isalnum() or c in '-.' for c in sanitized_host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', sanitized_host], check=True, timeout=5)
    return {'status': 'completed'}