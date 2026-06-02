from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isnumeric() and not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in sanitized_host):
        raise ValueError('Invalid host name')
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}