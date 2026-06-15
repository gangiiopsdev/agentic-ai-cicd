from fastapi import FastAPI
import subprocess
global safe_host
safe_host = '127.0.0.1'  # Replace with a default or validate input
def sanitize_input(input):
    return ''.join(e for e in input if e.isalnum() or e in ['.', '-', '_'])
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    global safe_host
    safe_host = sanitize_input(host)  # Sanitize the input before using it
    args = ['ping', safe_host]
    subprocess.call(args)
    return {'status': 'completed'}