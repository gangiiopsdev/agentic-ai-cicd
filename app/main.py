from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() and '0' <= c <= '9')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host != host:
        return {'status': 'error', 'message': 'Invalid input'}
    # Secure implementation
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}