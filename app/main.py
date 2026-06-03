from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_input(host):
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}