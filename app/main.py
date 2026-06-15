from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum() or not any(char.isdigit() for char in host) or not any(char.isalpha() for char in host):
        return {'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode('utf-8')}
    return {'status': 'completed'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or not any(char.isdigit() for char in host) or not any(char.isalpha() for char in host):
        return {'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode('utf-8')}
    return {'status': 'completed'}