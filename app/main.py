from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}