from fastapi import FastAPI
import subprocess
def sanitize_input(value):
    return ''.join(e for e in value if e.isalnum() or e in ('.', '-', '_'))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}