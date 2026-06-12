from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    sanitized = ''.join(e for e in input_str if e.isalnum() or e in ['.', '-', '_'])
    return sanitized

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = sanitize_input(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}